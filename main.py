import psutil
from time import sleep

def get_all_gta_pids():
  process_name = 'GTA5'
  pids = []
  for proc in psutil.process_iter():
    if process_name in proc.name():
      pids.append(proc.pid)
  return pids

def pause_all_processes_with_pid(pids):
  for proc in psutil.process_iter():
    if(proc.pid in pids):
      proc.suspend()

def resume_all_processes_with_pid(pids):
  for proc in psutil.process_iter():
    if(proc.pid in pids):
      proc.resume()

def execute():
  print("Feito por Bruno Barros Mello")
  print("----------------------------")
  print()
  
  pids = get_all_gta_pids()

  if(len(pids) > 0):
    pause_all_processes_with_pid(pids)
    sleep(11)
    resume_all_processes_with_pid(pids)
    print("Finalizado")
  else:
    print("Não encontrei nenhuma instância de GTA5 em execução")

execute()