def __hash(key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
            print(my_hash)
        return my_hash


__hash('bolts')