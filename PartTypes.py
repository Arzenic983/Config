class Part:
    def __init__(self, price, m):
        self.price = price
        self.manufacturer = m



class CPU(Part):
    def __init__(self, price, m, s, t, cores, threads):
        super().__init__(price, m)
        self.socket = s
        self.tdp = t
        self.core = cores
        self.thread = threads

    def da_print(self, name):
        self.name = name
        return f"""
    Процессор {name}:
    - Цена: {self.price}
    - Производитель: {self.manufacturer}
    - Сокет: {self.socket}
    - Теплопакет: {self.tdp}
    - Ядра/Потоки: {self.core}/{self.thread}
        """


class MTRBRD(Part):
    def __init__(self, price, m, soc, chip, freq, slots, channels, pci, ddr, pins, rgb):
        super().__init__(price, m)
        self.socket = soc
        self.chipset = chip
        self.mem_freq = freq
        self.slots = slots
        self.channels = channels
        self.pci_e = pci
        self.mem_type = ddr
        self.cpu_pin = pins
        self.rgb = rgb

    def da_print(self, name):
        self.name = name
        return f"""
    Материнская плата {name}:                                
    - Цена: {self.price}                                      
    - Производитель: {self.manufacturer}                     
    - Сокет: {self.socket}                                    
    - Чипсет: {self.chipset}                                  
    - Частота контроллера памяти: {self.mem_freq}            
    - Количество слотов ОЗУ: {self.slots} 
    - Количество каналов ОЗУ: {self.channels}
    - Версия PCI-E: {self.pci_e} 
    - Тип оперативной памяти: {self.mem_type}
    - Питание процессора: {self.cpu_pin}
    - Подсветка: {self.rgb} 
        """


class GPU(Part):
    def __init__(self, price, m, pci, chip, vram, gddr, rgb, tdp, pins):
        super().__init__(price, m)
        self.pci_e = pci
        self.g_chip = chip
        self.vram_size = vram
        self.mem_type = gddr
        self.rgb = rgb
        self.tdp = tdp
        self.gpu_pin = pins

    def da_print(self, name):
        self.name = name
        return f"""
    Графический ускоритель {name}:
    - Цена: {self.price}
    - Производитель: {self.manufacturer}                    
    - Версия PCI-E: {self.pci_e}                            
    - Наименование графического чипа: {self.g_chip}         
    - Объём видеопамяти: {self.vram_size}                   
    - Тип видеопамяти: {self.mem_type}
    - Теплопакет: {self.tdp}
    - Дополнительное питание: {self.gpu_pin}
    - Подсветка: {self.rgb}
        """


class RAM(Part):
    def __init__(self, price, m, gb, n, ddr, rgb, lat):
        super().__init__(price, m)
        self.size = gb
        self.count = n
        self.mem_type = ddr
        self.rgb = rgb
        self.timings = lat

    def da_print(self, name):
        self.name = name
        return f""" 
    Оперативное запоминающее устройство {name}:
    - Цена: {self.price}
    - Производитель: {self.manufacturer}                    
    - Объём комплекта: {self.size}                          
    - Количество модулей: {self.count}
    - Тип памяти: {self.mem_type}
    - Подсветка модулей: {self.rgb}
    - Частота и тайминги: {self.timings}
        """


class COOLER(Part):
    def __init__(self, price, m, rgb, tdp, tower, soc):
        super().__init__(price, m)
        self.rgb = rgb
        self.tdp = tdp
        self.type = tower
        self.soc = soc

    def da_print(self, name):
        self.name = name
        return f""" 
    Процессорный кулер {name}:
    - Цена: {self.price} 
    - Производитель: {self.manufacturer}                    
    - Рассеивает тепла: {self.tdp}                          
    - Подсветка: {self.rgb}
    - Тип: {self.type}
    - Сокет: {self.soc}
        """


class CORPUS(Part):
    def __init__(self, price, m, rgb, size, pw_spl):
        super().__init__(price, m)
        self.rgb = rgb
        self.formfactor = size
        self.pwr_spl_place = pw_spl

    def da_print(self, name):
        self.name = name
        return f"""
    Корпус компьютера {name}:
    - Цена: {self.price}
    - Производитель: {self.manufacturer}
    - Формфактор: {self.formfactor}
    - Расположение блока питания: {self.pwr_spl_place}
    - Подсветка: {self.rgb}
        """


class STRG(Part):
    def __init__(self, price, m, size, var):
        super().__init__(price, m)
        self.size = size
        self.variation = var

    def da_print(self, name):
        self.name = name
        return f"""
    Накопитель данных {name}:
    - Цена: {self.price}
    - Производитель: {self.manufacturer}
    - Объём: {self.size}
    - Тип: {self.variation}
        """


class PWRSPL(Part):
    def __init__(self, price, m, rgb, watts, cpu, gpu):
        super().__init__(price, m)
        self.rgb = rgb
        self.power = watts
        self.cpu_pin = cpu
        self.gpu_pin = gpu

    def da_print(self, name):
        self.name = name
        return f"""
        Блок питания {name}: 
        - Цена: {self.price}                              
        - Производитель: {self.manufacturer}             
        - Мощность: {self.power}                        
        - Питание на процессор: {self.cpu_pin}
        - Питание на видеокарту: {self.gpu_pin}
        - Подсветка: {self.rgb}
        """
