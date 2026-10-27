"""Valida un CSV demostrativo y genera un tablero estático sin dependencias."""
import argparse
import csv
import html
from pathlib import Path

FIELDS = ['op', 'planta', 'cantidad', 'estado']
STATES = {'Pendiente', 'En proceso', 'Terminado'}

def cargar(path):
    with open(path, encoding='utf-8', newline='') as source:
        reader = csv.DictReader(source)
        if reader.fieldnames != FIELDS:
            raise ValueError('Columnas esperadas: ' + ','.join(FIELDS))
        rows, seen = [], set()
        for line, row in enumerate(reader, 2):
            if None in row or any(v is None or not v.strip() for v in row.values()):
                raise ValueError(f'Fila {line}: campos vacíos o columnas adicionales')
            row = {k: v.strip() for k, v in row.items()}
            if row['op'] in seen:
                raise ValueError(f'Fila {line}: OP duplicada')
            if row['planta'] not in {'1323', '1170', 'Chincha'}:
                raise ValueError(f'Fila {line}: planta desconocida')
            if row['estado'] not in STATES:
                raise ValueError(f'Fila {line}: estado desconocido')
            try:
                row['cantidad'] = int(row['cantidad'])
            except ValueError:
                raise ValueError(f'Fila {line}: cantidad no entera') from None
            if row['cantidad'] <= 0:
                raise ValueError(f'Fila {line}: cantidad debe ser positiva')
            seen.add(row['op'])
            rows.append(row)
    if not rows:
        raise ValueError('No hay órdenes para procesar')
    return rows

def generar(rows, output):
    total = sum(r['cantidad'] for r in rows)
    finished = sum(r['cantidad'] for r in rows if r['estado'] == 'Terminado')
    body = ''.join('<tr>' + ''.join('<td>' + html.escape(str(r[k])) + '</td>' for k in FIELDS) + '</tr>' for r in rows)
    page = '''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
    <title>Control de lavandería | DataOps</title><style>
    body{font:16px system-ui;background:#f0f4f8;color:#16324f;margin:0}main{max-width:960px;margin:auto;padding:32px 20px}
    h1{font-size:34px} .cards{display:flex;gap:16px;flex-wrap:wrap}.card{background:white;padding:20px;border-radius:14px;flex:1;min-width:180px}.card strong{display:block;font-size:30px}
    .table{overflow:auto;background:white;border-radius:14px;margin-top:24px}table{border-collapse:collapse;width:100%}th,td{text-align:left;padding:16px;border-bottom:1px solid #e4eaf0}th{background:#16324f;color:white}footer{margin-top:24px;color:#526575}
    </style><main><p>PROYECTO ACADÉMICO / DATAOPS</p><h1>Control de lavandería</h1>
    <p>Seguimiento de órdenes por planta. Datos ficticios para demostración.</p>
    <div class="cards"><div class="card">Órdenes<strong>''' + str(len(rows)) + '''</strong></div><div class="card">Prendas programadas<strong>''' + f'{total:,}' + '''</strong></div><div class="card">Prendas terminadas<strong>''' + f'{finished:,}' + '''</strong></div></div>
    <div class="table"><table><thead><tr><th>OP</th><th>Planta</th><th>Cantidad</th><th>Estado</th></tr></thead><tbody>''' + body + '''</tbody></table></div>
    <footer>Angelo Zambrano · Curso DataOps · Versión 1.0<br>La tabla refleja el CSV versionado; no es una conexión al sistema de la empresa.</footer></main></html>'''
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(page, encoding='utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='datos/ordenes.csv')
    parser.add_argument('--output', default='docs/index.html')
    args = parser.parse_args()
    try:
        rows = cargar(args.input)
        generar(rows, args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f'Validación fallida: {error}\n')
    print(f'Validación correcta: {len(rows)} órdenes; tablero generado en {args.output}')
