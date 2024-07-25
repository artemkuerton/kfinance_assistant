# KFinance Assistant

[![PyPI](https://img.shields.io/pypi/v/kfinance-assistant)](https://pypi.org/project/kfinance-assistant/)
[![Docs](https://img.shields.io/badge/docs-latest-blue)]()
![GitHub](https://img.shields.io/github/license/artemkuerton/kfinance_assistant)
![GitHub last commit](https://img.shields.io/github/last-commit/artemkuerton/kfinance_assistant)

Система для управления финансами и анализа расходов.

- [Документация]()
- [Основной репозиторий с документацией]()
- [Документация для разработчиков]()

## Начало работы

<!-- termynal -->

```
$ pip install kfinance-assistant
```

## Возможности

- &#9745; Добавление транзакций
- &#9745; Установка бюджета
- &#9745; Анализ расходов
- &#9745; Статус бюджета

## Как пользоваться

Вот пример, как использовать библиотеку `KFinanceAssistant` для управления вашими финансами:

### Шаг 1: Установка библиотеки

Сначала установите библиотеку, если вы еще этого не сделали:

<!-- termynal -->

```
$ pip install kfinance-assistant
```

### Шаг 2: Импортируйте библиотеку

Теперь вы можете импортировать `KFinanceAssistant` в своем Python-скрипте:

```python
from kfinance_assistant import KFinanceAssistant
```

### Шаг 3: Создайте объект класса

Создайте экземпляр класса `KFinanceAssistant`:

```python
assistant = KFinanceAssistant()
```

### Шаг 4: Добавление транзакций

Вы можете добавлять транзакции, передавая отрицательные значения для расходов и положительные для доходов:

```python
assistant.add_transaction(-100, 'Питание')   # Расход 100 на питание
assistant.add_transaction(200, 'Заработок')   # Доход 200
assistant.add_transaction(-50, 'Транспорт')    # Расход 50 на транспорт
```

### Шаг 5: Установка бюджета

Установите свой бюджет, чтобы контролировать расходы:

```python
assistant.set_budget(500)  # Устанавливаем бюджет на уровне 500
```

### Шаг 6: Анализ расходов

Запустите анализ расходов, чтобы получить отчет:

```python
assistant.analyze_expenses()
```

### Шаг 7: Проверка статуса бюджета

Проверьте текущий статус бюджета:

```python
assistant.budget_status()
```

## Пример полного использования

Вот полное пример использования библиотеки:

```python
from kfinance_assistant import KFinanceAssistant

# Создаем экземпляр помощника по финансам
assistant = KFinanceAssistant()

# Добавляем транзакции
assistant.add_transaction(-100, 'Питание')
assistant.add_transaction(-50, 'Транспорт')
assistant.add_transaction(300, 'Заработок')

# Устанавливаем бюджет
assistant.set_budget(500)

# Анализируем расходы
assistant.analyze_expenses()

# Проверяем статус бюджета
assistant.budget_status()
```

После выполнения кода выше, вы получите отчет о своих расходах, преимущества, как сохранить свой бюджет, а также текущее состояние ваших финансов.

Эта библиотека поможет вам легко управлять своими финансами и принимать более осознанные решения о расходах и доходах. Надеюсь, это поможет вам успешно начать использовать `KFinance Assistant`!

## Contribution

Для тех, кто хочет внести свои изменения в проект.

- [CONTRIBUTING](https://github.com/artemkuerton/kfinance_assistant/blob/main/CONTRIBUTING.md)

## License

Лицензия [MIT License](https://github.com/artemkuerton/kfinance_assistant/blob/main/LICENSE).
