class Category:
    def __init__(self, category):
        self.category = category
        self.init_ledger()

    def init_ledger(self):
        self.ledger = [{
            "amount": 0,
            "description": ''
        }, {
            "amount": 0,
            "description": ''
        }, {
            "amount": 0,
            "description": ''
        }]

    def deposit(self, budget, type=''):
        ledger = {"amount": budget, "description": type}
        self.ledger[0] = ledger

    def withdraw(self, price, items=''):

        fundable = self.check_funds(price)
        if (fundable):
            ledger = {"amount": price * -1, "description": items}
            self.ledger[1] = ledger
            return True

        return False

    def get_balance(self):
        budget = self.ledger[0]["amount"]
        expense = self.ledger[1]["amount"]
        return budget + expense

    def transfer(self, amount, other_category):
        fundable = self.check_funds(amount)
        if (fundable):
            description = "Transfer to " + other_category.category
            ledger = {"amount": amount * -1, "description": description}
            self.ledger[2] = ledger
            other_category.deposit(amount, "Transfer from " + self.category)
            return True

        return False

    def check_funds(self, amount):
        budget = self.ledger[0]["amount"]

        return budget >= amount

    def __str__(self):
        deposit = self.ledger[0]
        withdraw = self.ledger[1]
        transfar = self.ledger[2]
        rest = deposit["amount"] + transfar["amount"] + withdraw["amount"]

        result = ("*************" + self.category + "*************\n" +
                  "deposit                 " +
                  '{:.2f}'.format(deposit["amount"]) + "\n" +
                  withdraw["description"][0:23] + ' ' +
                  '{:.2f}'.format(withdraw["amount"]) + "\n" +
                  transfar["description"][0:23] + ' ' +
                  '{:.2f}'.format(transfar["amount"]) + "\n" + "Total: " +
                  str(rest))
        return result

    def spent_percentage(self, total):
        withdraw = self.ledger[1]["amount"] * -1
        return (withdraw / total) * 100

    def spent_number(self, percentage):
        num = 0
        for i in range(0, 9):
            if percentage > 10 * i:
                num += 1
        return num

    def spent_graph(self, total):
        percentage = self.spent_percentage(total)
        spent_number = self.spent_number(percentage)
        dots = []
        for i in range(spent_number):
            dots.append('o')
        return dots


def generate_lavels(categories, length):
    category_names = []
    for category in categories:
        category_names.append(category.category.ljust(length))
    return category_names


def max_name_category(categories):
    category_names = []
    for category in categories:
        category_names.append(len(category.category))
    return max(category_names)


def create_spend_chart(categories):
    # チャートのタイトル
    chart = "Percentage spent by category\n"

    # カテゴリごとのチャートのラベル用生成
    length = max_name_category(categories)
    labels = generate_lavels(categories, length)

    # 消費の合計を取得
    total = 0
    for cat in categories:
        total += cat.ledger[1]["amount"] * -1

    # グラフのメイン部分
    for c in range(10, -1, -1):
        # Y軸のメモリを生成（上から、100 -> 0)
        chart += str(c * 10).rjust(3) + "| "
        for cat in categories:
            graph = cat.spent_graph(total)
            append = " "
            if (len(graph) > c):
                append = graph[c - 1]
            chart += append + "  "
        chart += "\n"
    chart += "    -" + "---" * len(categories) + "\n"

    # チャートのX軸のラベルを描画
    for i in range(length):
        chart += "     "
        for label in labels:
            chart += label[i] + "  "
        if i < length - 1:
            chart += "\n"
    return chart
