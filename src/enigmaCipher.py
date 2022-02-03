from enigma.machine import EnigmaMachine

def initEnigma(wheelOrder, ringSettings, reflector, plugboardSettings):
    machine = EnigmaMachine.from_key_sheet(
        rotors = wheelOrder,
        ring_settings = ringSettings,
        reflector = reflector,
        plugboard_settings = plugboardSettings
    )
    return machine

def enigma(machine, initPosition, messageKey, inputText):
    machine.set_display(initPosition)
    messageKey = machine.process_text(messageKey)
    machine.set_display(messageKey)

    text = machine.process_text(inputText, replace_char='')

    return text

def rotorPosition(machine):
    return machine.get_display()

# machine = initEnigma('II IV V', 'B U L', 'B', 'AV BS CG DL FU HZ IN KM OW RX')
# print(enigma(machine, 'WXC', 'BLA', 'OZBBZFFBPHWCOINSDRJTKB'))
