N = int(input())
computers = []

for _ in range(N):
    name, cpu, gpu, disc, ram, price = input().split()
    computers.append({
        'name': name,
        'cpu': int(cpu),
        'gpu': int(gpu),
        'disc': int(disc),
        'ram': int(ram),
        'price': int(price)
    })


M = int(input())

for _ in range(M):
    requirements = {}
    req_pairs = input().strip().split()
    for pair in req_pairs:
        key, value = pair.split(":")
        requirements[key] = int(value)

    selected = []
    for computer in computers:
        select = True
        for key, value in requirements.items():
            if computer[key] < value:
                select = False
                break
        if select:
            selected.append(computer)

    selected.sort(key=lambda i: (i['price'], i['name']))
    print(selected[0]["name"])
