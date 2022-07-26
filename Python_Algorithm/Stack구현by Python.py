class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,val):
        self.items.append(val)
    
    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('스택이 비었습니다.')
    
    def __len__(self):
        return len(self.items)
    
    def top(self):
        try:
            return self.items[-1]
        
        except IndexError:
            print('스택이 비었습니다')
            
s = Stack()
s.push(4)
s.push(3)
s.push(2)
s.push(1)

print(f'스택 s의 상태는 {s.items}이다')

print(f'스택 s의 젤 위의 값은 {s.top()}이다')

print(f'스택 s의 길이는 {len(s)}이다')

print(f'{s.items.pop()}를 꺼낸다')

print(f's에 남은 값은 {s.items}이다.')

print(f'스택 s의 길이는 {len(s)}이다')

