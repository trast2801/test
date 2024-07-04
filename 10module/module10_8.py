from multiprocessing import Process, Manager


class WarehouseManager:
    def __init__(self, data):
        self.data = data

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            if product in self.data:
                self.data[product] += quantity
            else:
                self.data[product] = quantity
        elif action == "shipment":
            if product in self.data and self.data[product] >= quantity:
                self.data[product] -= quantity

    def run(self, requests):
        processes = []
        for request in requests:
            proc = Process(target=self.process_request, args=(request,))
            processes.append(proc)
            proc.start()
        for p in processes:
            p.join()


if __name__ == '__main__':
    manager = Manager()
    data = manager.dict()

    warehouse_manager = WarehouseManager(data)

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    warehouse_manager.run(requests)

    print(data)





