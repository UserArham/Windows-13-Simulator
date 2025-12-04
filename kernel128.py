class Kernel128:
    def __init__(self):
        self.registers = [0] * 32  # 32 simulated 128-bit registers
        self.memory_map = {}
        self.process_list = []
        self.next_pid = 1

    def allocate128(self, label, value):
        """Simulated 128-bit memory cell."""
        self.memory_map[label] = value & ((1 << 128) - 1)

    def read128(self, label):
        return self.memory_map.get(label, 0)

    def create_process(self, name):
        pid = self.next_pid
        self.next_pid += 1
        proc = {
            "pid": pid,
            "name": name,
            "state": "running",
            "registers": [0] * 32,
        }
        self.process_list.append(proc)
        return proc

    def tick(self):
        """Fake kernel time tick."""
        for p in self.process_list:
            p["registers"][0] += 1  # increment instruction counter
