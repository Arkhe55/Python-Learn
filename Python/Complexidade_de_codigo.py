velocidade = 60
local_carro = 100

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE= 1 #distancia onde o radar pega

Range_do_radar = LOCAL_1 - RADAR_RANGE
Range_do_radar_2 = LOCAL_1+ RADAR_RANGE

carro_ultrapassou_radar = velocidade > RADAR_1
carro_passou_no_radar_1 = local_carro >= Range_do_radar and \
    local_carro <= Range_do_radar_2
carro_multado_radar_1 = carro_ultrapassou_radar and carro_passou_no_radar_1

if carro_ultrapassou_radar:
    print('Velocidade carro ultrapassou o radar 1')
if carro_passou_no_radar_1:
    print('Carro passou no radar')
if carro_ultrapassou_radar:
    print('Você foi multado')

# if velocidade > RADAR_1:
#     print("Você ultrapasou a velocidade")
#     if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#         local_carro <= (LOCAL_1+ RADAR_RANGE):
#         print("Você foi multado")
    
    
