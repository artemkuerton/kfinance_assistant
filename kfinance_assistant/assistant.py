import json

class KFinanceAssistant:
    def __init__(self):
        """Инициализация финансового помощника."""
        self.transactions = []
        self.budget = 0 

    def add_transaction(self, amount, category):
        """Добавить операцию с указанной суммой и категорией."""
        self.transactions.append({'amount': amount, 'category': category})
        print(f"Операция добавлена: {amount} в категории '{category}'.")

    def set_budget(self, budget):
        """Установить бюджет пользователя."""
        self.budget = budget
        print(f"Бюджет установлен: {budget}.")

    def analyze_expenses(self):
        """Анализировать расходы и предоставить отчет."""
        total_expenses = sum(t['amount'] for t in self.transactions if t['amount'] < 0)
        expenses_by_category = {}

        for transaction in self.transactions:
            if transaction['amount'] < 0:
                category = transaction['category']
                if category not in expenses_by_category:
                    expenses_by_category[category] = 0
                expenses_by_category[category] += abs(transaction['amount'])

        print("\n====== Отчет по расходам ======")
        print(f"Общие расходы: {total_expenses}")
        for category, amount in expenses_by_category.items():
            print(f"{category}: {amount}")
        print("===============================")

        if total_expenses > self.budget:
            print("Вы превысили бюджет! Рассмотрите возможность сокращения расходов.")
        else:
            print("Вы в пределах бюджета.")

    def budget_status(self):
        """Проверить статус бюджета."""
        total_expense = sum(t['amount'] for t in self.transactions if t['amount'] < 0)
        balance = self.budget + total_expense
        print(f"Текущий баланс бюджета: {balance}.")
