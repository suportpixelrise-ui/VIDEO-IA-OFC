from pathlib import Path
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r'C:\Users\Michael\.codex\attachments\ad59b65a-eef8-4e0e-9e37-c33ee7a99f03\Texto colado.txt')
for folder in ['docs', 'public/assets', 'public/audio/locucao', 'scripts', 'renders/qa']:
    (ROOT/folder).mkdir(parents=True, exist_ok=True)
text = SOURCE.read_text(encoding='utf-8-sig')
(ROOT/'docs/prompt-mestre-original.txt').write_text(text, encoding='utf-8')
narration = text.split('TEXTO DE LOCUÇÃO:',1)[1].split('DIREÇÃO DA VOZ',1)[0].strip().strip('“”').strip()
paragraphs = [p.strip() for p in narration.split('\n\n') if p.strip()]
pauses = [0.6,0.5,0.4,0.5,0.55,0.9,0.3,0.45,0.7,1.0,1.2,0.35,0.3,0.6,0.4,0.4,0.4,0.9]
segments = [{'id': f'{i:02d}', 'text': p, 'pause_after': pauses[i] if i<len(pauses) else 0.4} for i,p in enumerate(paragraphs)]
(ROOT/'docs/narracao.txt').write_text(narration+'\n', encoding='utf-8')
(ROOT/'docs/segmentos-locucao.json').write_text(json.dumps(segments,ensure_ascii=False,indent=2),encoding='utf-8')
for image in (ROOT.parent/'referencias').glob('*.png'):
    shutil.copy2(image, ROOT/'public/assets'/image.name)
generated = Path.home()/'.codex/generated_images/01a1570d-a4b3-7dc2-b83c-1cfd9e910ad7'
for source, dest in [
    ('exec-2daa3e71-0f8b-41df-ad84-a8ad2c20d91b.png','lia-rig.png'),
    ('exec-51592af6-2326-4278-8316-94ac605bdc3c.png','caio-rig.png')]:
    shutil.copy2(generated/source, ROOT/'public/assets'/dest)
print(f'{len(segments)} blocos de locução, {len(narration.split())} palavras. Referências e rigs preservados no projeto.')
