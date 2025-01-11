def load_ips(file_path):
    with open(file_path, 'r') as f:
        return list(line.strip() for line in f)

def remove_duplicates(ip_list):
    from collections import OrderedDict
    unique_ips = list(OrderedDict.fromkeys(ip_list))
    
    print("すべてのIPアドレス:")
    print(ip_list)
    
    print("\nユニークなIPアドレス:")
    print(unique_ips)
    
    duplicates = [ip for ip in ip_list if ip_list.count(ip) > 1]
    duplicates = list(set(duplicates))
    print("\n重複しているIPアドレス:")
    print(duplicates)
    
    return unique_ips

if __name__ == "__main__":
    file_path = "bad-ips.txt"
    
    ip_list = load_ips(file_path)
    
    unique_ips = remove_duplicates(ip_list)
    
    with open(file_path, 'w') as f:
        for ip in unique_ips:
            f.write(f"{ip}\n")
