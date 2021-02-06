import copy

import socketio

import bluetooth as bt
import constants as cte

ser = bt.connect_duel_disk()
sio = socketio.Client()

sio.connect(f'http://127.0.0.1:{cte.SMART_DUEL_SERVER_PORT}')

card_id = ''
while card_id != cte.NEXT_PHASE:
    card_id = bt.select_card_id(ser)
    if card_id not in [cte.NEXT_PHASE, cte.BACK]:
        data = copy.deepcopy(cte.SUMMON_DATA)
        data['yugiohCardId'] = card_id
        data['zoneName'] = 'mainMonster1'
        sio.emit('summonEvent', data=data)
