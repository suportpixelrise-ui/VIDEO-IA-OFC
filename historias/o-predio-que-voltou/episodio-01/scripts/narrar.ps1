$ErrorActionPreference = 'Stop'
$episodeRoot = Split-Path $PSScriptRoot -Parent
Add-Type -AssemblyName System.Speech
$speechReferences = @((Get-ChildItem -LiteralPath (Join-Path $PSHOME 'ref') -Filter '*.dll').FullName)
$speechReferences += [System.Speech.Synthesis.SpeechSynthesizer].Assembly.Location
Add-Type -ReferencedAssemblies $speechReferences -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Speech.Synthesis;
public class EpisodeWord {
    public double Start {get;set;}
    public string Text {get;set;}
    public int Char {get;set;}
    public int Count {get;set;}
}
public static class EpisodeNarration {
    public static EpisodeWord[] Speak(string text, string output) {
        var words = new List<EpisodeWord>();
        using(var voice = new SpeechSynthesizer()) {
            voice.SelectVoice("Microsoft Maria Desktop");
            voice.Rate = 0;
            voice.Volume = 100;
            voice.SpeakProgress += delegate(object sender, SpeakProgressEventArgs e) {
                lock(words) words.Add(new EpisodeWord { Start=e.AudioPosition.TotalSeconds, Text=e.Text, Char=e.CharacterPosition, Count=e.CharacterCount });
            };
            voice.SetOutputToWaveFile(output);
            voice.Speak(text);
            voice.SetOutputToNull();
        }
        return words.ToArray();
    }
}
'@
$segments = Get-Content -LiteralPath (Join-Path $episodeRoot 'docs\segmentos-locucao.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$wordData = @()
foreach ($segment in $segments) {
    $wavPath = Join-Path $episodeRoot ('public\audio\locucao\' + $segment.id + '.wav')
    $words = [EpisodeNarration]::Speak($segment.text, $wavPath)
    $wordData += [pscustomobject]@{ id=$segment.id; words=@($words) }
    Write-Output ('Locucao ' + $segment.id + ' pronta.')
}
$wordData | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath (Join-Path $episodeRoot 'docs\palavras-locucao-local.json') -Encoding UTF8
