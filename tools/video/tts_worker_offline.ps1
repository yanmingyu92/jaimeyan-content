param(
  [Parameter(Mandatory = $true)][string]$JobFile,
  [Parameter(Mandatory = $true)][string]$Ffmpeg,
  [Parameter(Mandatory = $true)][string]$Ffprobe
)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$job = Get-Content -LiteralPath $JobFile -Raw -Encoding UTF8 | ConvertFrom-Json
$failures = @()

foreach ($seg in $job.segments) {
  $wav = [System.IO.Path]::ChangeExtension($seg.mp3, '.wav')
  try {
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    try {
      if ($seg.rate -match '^([+-]?\d+)%$') {
        $percent = [int]$Matches[1]
        $synth.Rate = [Math]::Max(-10, [Math]::Min(10, [int]($percent / 10)))
      }
      $synth.SetOutputToWaveFile($wav)
      $synth.Speak($seg.text)
    } finally {
      $synth.Dispose()
    }
    & $Ffmpeg -v error -y -i $wav -codec:a libmp3lame -qscale:a 3 $seg.mp3
    if ($LASTEXITCODE -ne 0) { throw "ffmpeg exited $LASTEXITCODE" }
    $durationText = (& $Ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $seg.mp3) | Select-Object -First 1
    $duration = [double]::Parse($durationText, [Globalization.CultureInfo]::InvariantCulture)
    $events = @(@{ t = $seg.text; o = 0; d = [long]($duration * 10000000) })
    $json = $events | ConvertTo-Json -Compress
    [System.IO.File]::WriteAllText($seg.words, $json, [System.Text.UTF8Encoding]::new($false))
  } catch {
    $failures += "$($seg.id): $($_.Exception.Message)"
    Remove-Item -LiteralPath $seg.mp3, $seg.words -ErrorAction SilentlyContinue
  } finally {
    Remove-Item -LiteralPath $wav -ErrorAction SilentlyContinue
  }
}

if ($failures.Count) {
  $failures | ForEach-Object { Write-Error "FAILED $_" }
  exit 1
}
Write-Output "OK $($job.segments.Count) offline Windows SAPI segments"
