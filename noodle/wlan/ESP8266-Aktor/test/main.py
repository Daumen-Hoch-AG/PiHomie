from machine import Pin
#in1 = Pin12
#in2 = Pin13
#out1 = Pin4
#out2 = Pin5

b_up = Pin(12,Pin.IN)
b_down = Pin(13,Pin.IN)
m_up = Pin(4,Pin.OUT)
m_down = Pin(5,Pin.OUT)


def up_callback(p):
    print("Interrupt für Pin {}".format(p))
    if m_up.value() == 1:
        m_up.off()
    else:
        m_up.on()

def ein(p):
	if p.value() == 1:
		stamp = time.time()
		time.sleep(1.1)
		while stamp != 0:
			print(‚Roll…’)
			time.sleep(1)
	if p.value() == 0:
		delta = time.time() - stamp
		if delta <= 1:
			print(„Roll until end“)
			stamp = 0

b_up.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=up_callback)