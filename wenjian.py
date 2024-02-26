def open_wf(name,write):#写入txt（覆盖）
  str(write)
  with open(name,"w",encoding="utf-8") as f:
    f.write(write)
    f.close()
  return True
def open_wj(name,write):#写入txt（不覆盖）
  str(write)
  with open(name,"a",encoding="utf-8") as f:
    f.write(write+'\n')
    f.close()
  return True
def open_r(name):#读取（仅第一行）
    with open (name,"r",encoding="utf-8") as f:
        data = f.readline()
        f.close()
    return data
def open_r1(name):#全部读取
    with open (name,"r",encoding="utf-8") as f:
        data = f.readlines()
        f.close()
    return data