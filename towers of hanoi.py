def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} → {destination}")
    towers_of_hanoi(n - 1, auxiliary, source, destination)

# Example: 3 disks
n = 3
print(f"Towers of Hanoi Solution for {n} disks:\n")
towers_of_hanoi(n, 'A', 'B', 'C')
