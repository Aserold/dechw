import os
import time

def logger(path):
    
    
    def __logger(old_function):
        
        
        def new_function(*args, **kwargs):
            starttime = time.strftime("%a %d %b %Y, %H:%M:%S")
            
            result = old_function(*args, **kwargs)
            
            msg = f'Функция {old_function.__name__} вызвана: {starttime}, \nС аргументами: {args}, {kwargs}.\nРезультат: {result.__name__}'
            
            
            if os.path.exists(path):
                with open(path, 'a', encoding='utf-8') as f:
                    f.write(f'{msg}\n')
                
            else:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(f'{msg}\n')
            
            
            return result

        return new_function

    return __logger

def main():
    
    @logger('main.log')
    def flat_generator(list_of_lists):
        for item in list_of_lists:
            for sub_item in item:
                yield sub_item
                
    flat_generator([["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]])
    
            
    

if __name__ == '__main__':
    main()