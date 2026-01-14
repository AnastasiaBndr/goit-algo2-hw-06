def check_password_uniqueness(bloom,new_passwords:list)->list:
    results={i : "вже використаний" if bloom.contains(i) else "унікальний" for i in new_passwords}

    return results