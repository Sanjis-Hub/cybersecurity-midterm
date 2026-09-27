import argparse
import socket
import time

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "scanme.nmap.org"}
DEFAULT_TIMEOUT = 1.0
DEFAULT_DELAY = 0.05


def validate_target(host):
    """Allow only hosts authorized for this class assignment."""
    if host not in ALLOWED_HOSTS:
        raise ValueError(
            "Target not authorized. Use 127.0.0.1, localhost, or scanme.nmap.org."
        )


def validate_port_range(start_port, end_port):
    """Validate that the requested TCP port range is valid."""
    if not 1 <= start_port <= 65535:
        raise ValueError("Start port must be between 1 and 65535.")
    if not 1 <= end_port <= 65535:
        raise ValueError("End port must be between 1 and 65535.")
    if start_port > end_port:
        raise ValueError("Start port cannot be greater than end port.")


def scan_port(host, port, timeout=DEFAULT_TIMEOUT):
    """Try a TCP connection to one port and return its status."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

            if result == 0:
                return "OPEN"
            return "CLOSED"

    except socket.gaierror:
        return "ERROR: host could not be resolved"
    except socket.timeout:
        return "CLOSED/TIMEOUT"
    except OSError as error:
        return f"ERROR: {error}"


def scan_ports(host, start_port, end_port, timeout=DEFAULT_TIMEOUT, delay=DEFAULT_DELAY):
    """Scan an authorized host over an inclusive TCP port range."""
    validate_target(host)
    validate_port_range(start_port, end_port)

    print(f"Scanning {host} ports {start_port}-{end_port}")
    print(f"Timeout: {timeout:.1f}s | Delay: {delay:.2f}s")
    print("-" * 45)

    open_ports = []
    start_time = time.perf_counter()

    for port in range(start_port, end_port + 1):
        status = scan_port(host, port, timeout)

        if status == "OPEN":
            open_ports.append(port)

        print(f"Port {port:5d}: {status}")
        time.sleep(delay)

    elapsed = time.perf_counter() - start_time

    print("-" * 45)
    print(f"Scan complete in {elapsed:.2f} seconds.")
    print(f"Open ports: {open_ports if open_ports else 'None found'}")

    return open_ports


def main():
    parser = argparse.ArgumentParser(
        description="Authorized TCP port scanner for the cybersecurity midterm."
    )
    parser.add_argument(
        "host",
        help="Authorized target: 127.0.0.1, localhost, or scanme.nmap.org",
    )
    parser.add_argument("start_port", type=int, help="First port to scan (1-65535)")
    parser.add_argument("end_port", type=int, help="Last port to scan (1-65535)")
    parser.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT,
        help="Socket timeout in seconds (default: 1.0)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=DEFAULT_DELAY,
        help="Delay between port attempts in seconds (default: 0.05)",
    )

    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("Timeout must be greater than 0.")
    if args.delay < 0:
        parser.error("Delay cannot be negative.")

    try:
        scan_ports(
            args.host,
            args.start_port,
            args.end_port,
            args.timeout,
            args.delay,
        )
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
