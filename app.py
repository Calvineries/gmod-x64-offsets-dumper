from pymem import Pymem, process, pattern

print("...")
def get_sig(module_name, _pattern):
    memory = Pymem("gmod.exe")
    module = process.module_from_name(memory.process_handle, module_name)
    result = pattern.pattern_scan_module(memory.process_handle, module, _pattern)
    result += 0 - module.lpBaseOfDll
    return result


try:
    dwLocalPlayer = get_sig('client.dll', rb'......\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xFF\xFF\xFF\xFF\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\xFF\xFF\xFF\xFF')
except Exception as err:
    pass
try:
    dwEntityList = get_sig('client.dll', rb'\x00.....\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00.....\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00.....\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00.....\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00\x00....\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00.....\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00..\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00')
except Exception as err:
    pass
try:
    dwViewMatrix = get_sig('engine.dll', rb'......\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00......\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00......\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00......\x00\x00......\x00\x00..\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00......\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')    
except Exception as err:
    pass
try:
    dwForceAttack = get_sig('client.dll', rb'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.....\x7F\x00\x00.....\x7F\x00\x00')
except Exception as err:
    pass
try:
    dwForceJump = get_sig('client.dll', rb'\x04\x00\x00\x00\x00\x00\x00\x00....\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00.')
except Exception as err:
    pass


try:
    print("dwLocalPlayer:", hex(dwLocalPlayer))
except Exception as err:
    pass
try:
    print("dwEntityList:", hex(dwEntityList))
except Exception as err:
    pass
try:
    print("dwViewMatrix:", hex(dwViewMatrix))
except Exception as err:
    pass
try:
    print("dwForceAttack:", hex(dwForceAttack))
except Exception as err:
    pass
try:
    print("dwForceJump:", hex(dwForceJump))
except Exception as err:
    pass
