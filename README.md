# computer-networks-socket-programmingg

Mail transfer 
File transfer 
Go back n
Selective repeat


1. Mail Transfer: Mail transfer involves the exchange of electronic mail between users. Typically, this is achieved using protocols like SMTP (Simple Mail Transfer Protocol) for sending emails and IMAP (Internet Message Access Protocol) or POP3 (Post Office Protocol version 3) for receiving emails. SMTP is used by mail servers to send emails, while IMAP and POP3 are used by mail clients to retrieve emails from the server. These protocols define the rules and formats for communication between mail servers and clients.

2. File Transfer: File transfer involves transferring files from one location to another over a network. This can be achieved using various protocols such as FTP (File Transfer Protocol), SFTP (SSH File Transfer Protocol), HTTP (Hypertext Transfer Protocol), or even custom protocols built on top of TCP or UDP sockets. FTP is a standard protocol specifically designed for file transfer, while SFTP provides secure file transfer over SSH (Secure Shell). HTTP can also be used for file transfer, especially for web-based downloads.

3. Go-Back-N (GBN): Go-Back-N is a sliding window protocol used for reliable data transmission over an unreliable channel, such as a network with packet loss or corruption. In GBN, the sender sends a window of packets and waits for acknowledgments from the receiver. If an acknowledgment is not received within a timeout period, the sender retransmits all packets in the window starting from the oldest unacknowledged packet. GBN ensures that packets are delivered to the receiver in the correct order.

4. Selective Repeat: Selective Repeat is another sliding window protocol used for reliable data transmission. Unlike Go-Back-N, Selective Repeat allows the sender to retransmit only the packets that have been lost or corrupted, rather than retransmitting all packets in the window. This reduces unnecessary retransmissions and improves efficiency, especially in scenarios with low packet loss rates.

