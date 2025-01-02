all:
	@echo alimg
	@echo alup
	@echo alup-virgl
	@echo alup-virgl-whpx
	@echo clean

up:
	qemu-system-x86_64 \
		-smp 4 \
		-m 10G \
		-drive format=qcow2,file=alpine.qcow2,if=virtio \
		-device virtio-vga-gl \
		-display sdl,gl=on \
		-nic user,hostfwd=tcp::60022-:22 \
		-accel whpx,kernel-irqchip=off

alimg:
	qemu-img create -f qcow2 alpine.qcow2 10G
	qemu-system-x86_64 \
		-smp 2 \
		-m 4G \
		-drive format=qcow2,file=alpine.qcow2,if=virtio \
		-boot once=d \
		-cdrom alpine.iso


alup:
	qemu-system-x86_64 \
		-M q35 \
		-smp 2 \
		-m 4G \
		-drive format=qcow2,file=alpine.qcow2 

alup-virgl:
	qemu-system-x86_64 \
		-M q35 \
		-smp 2 \
		-m 4G \
		-drive format=qcow2,file=alpine.qcow2 \
		-vga virtio \
		-display gtk,grab-on-hover=on,gl=on

alup-virgl-sdl:
	qemu-system-x86_64 \
		-M q35 \
		-smp 2 \
		-m 4G \
		-drive format=qcow2,file=alpine.qcow2,id=blk1,if=none \
		-device virtio-vga-gl \
		-device virtio-blk-pci,drive=blk1 \
		-display sdl,gl=on

alup-virgl-sdl-ssh:
	qemu-system-x86_64 \
		-nic user,hostfwd=tcp::60022-:22 \
		-M q35 \
		-smp 2 \
		-m 4G \
		-drive format=qcow2,file=alpine.qcow2,id=blk1,if=none \
		-device virtio-vga-gl \
		-device virtio-blk-pci,drive=blk1 \
		-display sdl,gl=on

alup-virgl-accel:
	qemu-system-x86_64 \
		-M q35 \
		-smp 2 \
		-m 4G \
		-drive format=qcow2,file=alpine.qcow2 \
		-vga virtio \
		-display gtk,grab-on-hover=on,gl=on \
		-accel whpx,kernel-irqchip=off
