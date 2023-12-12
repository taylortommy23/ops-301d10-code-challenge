#!/usr/bin/env python3

import psutil

def get_system_info():
    # Get CPU times
    cpu_times = psutil.cpu_times()

    # Time spent by normal processes executing in user mode
    user_time = cpu_times.user

    # Time spent by processes executing in kernel mode
    system_time = cpu_times.system

    # Time when system was idle
    idle_time = cpu_times.idle

    # Time spent by priority processes executing in user mode
    nice_time = cpu_times.nice

    # Time spent waiting for I/O to complete
    io_wait_time = cpu_times.iowait

    # Time spent for servicing hardware interrupts
    irq_time = cpu_times.irq

    # Time spent for servicing software interrupts
    soft_irq_time = cpu_times.softirq

    # Time spent by other operating systems running in a virtualized environment
    steal_time = cpu_times.steal

    # Time spent running a virtual CPU for guest operating systems
    guest_time = cpu_times.guest

    print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
    print(f"Time spent by processes executing in kernel mode: {system_time} seconds")
    print(f"Time when system was idle: {idle_time} seconds")
    print(f"Time spent by priority processes executing in user mode: {nice_time} seconds")
    print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
    print(f"Time spent for servicing hardware interrupts: {irq_time} seconds")
    print(f"Time spent for servicing software interrupts: {soft_irq_time} seconds")
    print(f"Time spent by other operating systems running in a virtualized environment: {steal_time} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems: {guest_time} seconds")

if __name__ == "__main__":
    get_system_info()
