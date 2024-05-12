import time
import threading

class Sender:
    def __init__(self, window_size, timeout):
        self.window_size = window_size
        self.timeout = timeout
        self.base = 0
        self.next_seq_num = 0
        self.timer = None

    def start_timer(self):
        self.timer = threading.Timer(self.timeout, self.timeout_handler)
        self.timer.start()

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()

    def timeout_handler(self):
        print("Timeout occurred. Retransmitting packets from base to next_seq_num")
        self.start_timer()

    def send_packet(self):
        if self.next_seq_num < self.base + self.window_size:
            print(f"Sending packet with sequence number: {self.next_seq_num}")
            self.next_seq_num += 1
            if self.base == self.next_seq_num - self.window_size:
                self.start_timer()

    def receive_ack(self, ack_num):
        print(f"Received ACK for sequence number: {ack_num}")
        if ack_num >= self.base:
            self.base = ack_num + 1
            if self.base == self.next_seq_num:
                self.stop_timer()
            else:
                self.stop_timer()
                self.start_timer()


class Receiver:
    def __init__(self, window_size):
        self.window_size = window_size
        self.expected_seq_num = 0

    def receive_packet(self, seq_num):
        if seq_num == self.expected_seq_num:
            print(f"Received packet with sequence number: {seq_num}")
            self.expected_seq_num += 1
            return seq_num
        else:
            print(f"Discarding out-of-order packet with sequence number: {seq_num}")
            return -1

    def send_ack(self, ack_num):
        print(f"Sending ACK for sequence number: {ack_num}")


def simulate_network(sender, receiver, num_packets):
    for i in range(num_packets):
        sender.send_packet()
        time.sleep(1)
        ack_num = receiver.receive_packet(i)
        if ack_num != -1:
            sender.receive_ack(ack_num)
            receiver.send_ack(ack_num)


def main():
    window_size = 4
    timeout = 3
    sender = Sender(window_size, timeout)
    receiver = Receiver(window_size)

    num_packets = 10

    simulate_network(sender, receiver, num_packets)


if __name__ == "__main__":
    main()
