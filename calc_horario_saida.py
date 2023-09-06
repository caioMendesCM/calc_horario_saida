from datetime import datetime, timedelta
import sys
#considerando tempo sempre em min

def try_get(list, index, default):
  try:
    return list[index]
  except:
    return default

hoje = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

TEMPO_TOTAL_DIARIO = int(try_get(sys.argv, 4, 499))

param_entrada = try_get(sys.argv, 1, '09:00')
param_saida_almoco = try_get(sys.argv, 2, '12:00')
param_volta_almoco = try_get(sys.argv, 3, '13:00')


hora_entrada, min_entrada = map(int, param_entrada.split(':'))

hora_saida_almoco, min_saida_almoco = map(int, param_saida_almoco.split(':'))

hora_volta_almoco, min_volta_almoco = map(int, param_volta_almoco.split(':'))


entrada = hoje + timedelta(hours=hora_entrada, minutes=min_entrada)

saida_almoço = hoje + timedelta(hours=hora_saida_almoco, minutes=min_saida_almoco)

volta_almoço = hoje + timedelta(hours=hora_volta_almoco, minutes=min_volta_almoco)

tempo_pago_antes_almoço = (saida_almoço - entrada).total_seconds()

saida = volta_almoço + timedelta(minutes=TEMPO_TOTAL_DIARIO - (tempo_pago_antes_almoço/60))

print(str(saida.time())[:-3])