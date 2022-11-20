class Queue:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:

    def __init__(self, flavors, ):
        #attributes dont have to be passed within the parameter list
        self.flavors = flavors
        self.orders = Queue()
    def take_order(self , customer , flavor , scoops):
        if flavor not in  self.flavors:
            print(f"Sorry {customer}, all out of that {flavor}!")
        elif scoops in range(1, 4): 
            print(f"You want that {scoops} scoops?")
        else: 
            print ("Order created!!!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)
    def show_all_orders(self): 
        print("Pending Ice CReam Orders:")
        for order in self.orders.items:
     def next_order(self):
        print("Next order up!")
        order = self.orders.dequeue()
        print(order ['customer'])
shop = IceCreamShop(["rocky road" , "mint chip" , "pistachio"])
shop.take_order("Zach", "mint chip", 30)
shop.take_order("Tyler" , "rocky road" , 2)
shop.show_all_orders
shop.next_order()
shop.show_all_orders()