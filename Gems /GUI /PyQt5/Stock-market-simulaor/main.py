import sys
import random
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                            QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
                            QTabWidget, QMessageBox, QComboBox)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
import pyqtgraph as pg  # For charting - make sure to install with: pip install pyqtgraph

class StockMarketSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Market Simulator")
        self.setGeometry(100, 100, 1000, 800)

        # Initialize data
        self.portfolio = {}
        self.cash_balance = 100000.0
        self.stock_prices = {
            'AAPL': 150.0,
            'GOOGL': 2800.0,
            'MSFT': 300.0,
            'AMZN': 3300.0,
            'TSLA': 900.0
        }

        # Initialize historical data
        self.price_history = {symbol: {'times': [], 'prices': []} for symbol in self.stock_prices}
        self.start_time = datetime.now()

        # Set up the main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create tabs
        tabs = QTabWidget()
        layout.addWidget(tabs)

        # Market Tab
        market_tab = QWidget()
        market_layout = QVBoxLayout(market_tab)

        # Chart Section
        chart_widget = QWidget()
        chart_layout = QVBoxLayout(chart_widget)

        # Stock selector for chart
        chart_control_layout = QHBoxLayout()
        self.chart_symbol_selector = QComboBox()
        self.chart_symbol_selector.addItems(self.stock_prices.keys())
        self.chart_symbol_selector.currentTextChanged.connect(self.update_chart)
        chart_control_layout.addWidget(QLabel("Select Stock:"))
        chart_control_layout.addWidget(self.chart_symbol_selector)
        chart_control_layout.addStretch()
        chart_layout.addLayout(chart_control_layout)

        # Price Chart
        self.price_chart = pg.PlotWidget()
        self.price_chart.setBackground('w')
        self.price_chart.setTitle("Stock Price History")
        self.price_chart.setLabel('left', 'Price ($)')
        self.price_chart.setLabel('bottom', 'Time (seconds)')
        self.price_chart.showGrid(x=True, y=True)
        chart_layout.addWidget(self.price_chart)

        market_layout.addWidget(chart_widget)

        # Market Overview Table
        self.market_table = QTableWidget()
        self.market_table.setColumnCount(3)
        self.market_table.setHorizontalHeaderLabels(["Symbol", "Price", "Change"])
        market_layout.addWidget(self.market_table)

        # Trading Interface
        trade_layout = QHBoxLayout()
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("Stock Symbol")
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Quantity")

        buy_button = QPushButton("Buy")
        buy_button.clicked.connect(self.buy_stock)
        sell_button = QPushButton("Sell")
        sell_button.clicked.connect(self.sell_stock)

        trade_layout.addWidget(self.symbol_input)
        trade_layout.addWidget(self.quantity_input)
        trade_layout.addWidget(buy_button)
        trade_layout.addWidget(sell_button)
        market_layout.addLayout(trade_layout)

        # Portfolio Tab
        portfolio_tab = QWidget()
        portfolio_layout = QVBoxLayout(portfolio_tab)

        self.balance_label = QLabel(f"Cash Balance: ${self.cash_balance:,.2f}")
        portfolio_layout.addWidget(self.balance_label)

        self.portfolio_table = QTableWidget()
        self.portfolio_table.setColumnCount(4)
        self.portfolio_table.setHorizontalHeaderLabels(["Symbol", "Shares", "Avg Price", "Current Value"])
        portfolio_layout.addWidget(self.portfolio_table)

        # Add tabs
        tabs.addTab(market_tab, "Market")
        tabs.addTab(portfolio_tab, "Portfolio")

        # Setup timer for updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_prices)
        self.timer.start(2000)

        # Initial updates
        self.update_market_table()
        self.update_portfolio_table()

    def update_prices(self):
        current_time = (datetime.now() - self.start_time).total_seconds()

        for symbol in self.stock_prices:
            # Update current price
            change = random.uniform(-5, 5)
            self.stock_prices[symbol] *= (1 + change/100)

            # Update historical data
            self.price_history[symbol]['times'].append(current_time)
            self.price_history[symbol]['prices'].append(self.stock_prices[symbol])

            # Keep only last 50 data points for memory efficiency
            if len(self.price_history[symbol]['times']) > 50:
                self.price_history[symbol]['times'].pop(0)
                self.price_history[symbol]['prices'].pop(0)

        self.update_market_table()
        self.update_portfolio_table()
        self.update_chart()

    def update_chart(self):
        self.price_chart.clear()
        symbol = self.chart_symbol_selector.currentText()
        if symbol in self.price_history:
            self.price_chart.plot(
                self.price_history[symbol]['times'],
                self.price_history[symbol]['prices'],
                pen=pg.mkPen(color=(0, 0, 255), width=2)
            )
            self.price_chart.setTitle(f"{symbol} Price History")

    def update_market_table(self):
        self.market_table.setRowCount(len(self.stock_prices))
        for row, (symbol, price) in enumerate(self.stock_prices.items()):
            self.market_table.setItem(row, 0, QTableWidgetItem(symbol))
            self.market_table.setItem(row, 1, QTableWidgetItem(f"${price:,.2f}"))

            # Calculate price change
            if len(self.price_history[symbol]['prices']) > 1:
                prev_price = self.price_history[symbol]['prices'][-2]
                change = ((price - prev_price) / prev_price) * 100
            else:
                change = 0

            color = QColor(0, 255, 0) if change > 0 else QColor(255, 0, 0)
            change_item = QTableWidgetItem(f"{change:+.2f}%")
            change_item.setForeground(color)
            self.market_table.setItem(row, 2, change_item)

    def update_portfolio_table(self):
        self.portfolio_table.setRowCount(len(self.portfolio))
        total_value = self.cash_balance

        for row, (symbol, data) in enumerate(self.portfolio.items()):
            current_price = self.stock_prices.get(symbol, 0)
            current_value = data['shares'] * current_price
            total_value += current_value

            self.portfolio_table.setItem(row, 0, QTableWidgetItem(symbol))
            self.portfolio_table.setItem(row, 1, QTableWidgetItem(str(data['shares'])))
            self.portfolio_table.setItem(row, 2, QTableWidgetItem(f"${data['avg_price']:,.2f}"))
            self.portfolio_table.setItem(row, 3, QTableWidgetItem(f"${current_value:,.2f}"))

        self.balance_label.setText(f"Cash Balance: ${self.cash_balance:,.2f} | Total Portfolio Value: ${total_value:,.2f}")

    def buy_stock(self):
        symbol = self.symbol_input.text().upper()
        try:
            quantity = int(self.quantity_input.text())
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid quantity")
            return

        if symbol not in self.stock_prices:
            QMessageBox.warning(self, "Error", "Invalid stock symbol")
            return

        total_cost = quantity * self.stock_prices[symbol]
        if total_cost > self.cash_balance:
            QMessageBox.warning(self, "Error", "Insufficient funds")
            return

        if symbol in self.portfolio:
            current_shares = self.portfolio[symbol]['shares']
            current_avg_price = self.portfolio[symbol]['avg_price']
            new_total_shares = current_shares + quantity
            new_avg_price = ((current_shares * current_avg_price) + total_cost) / new_total_shares
            self.portfolio[symbol] = {'shares': new_total_shares, 'avg_price': new_avg_price}
        else:
            self.portfolio[symbol] = {'shares': quantity, 'avg_price': self.stock_prices[symbol]}

        self.cash_balance -= total_cost
        self.update_portfolio_table()
        self.symbol_input.clear()
        self.quantity_input.clear()

    def sell_stock(self):
        symbol = self.symbol_input.text().upper()
        try:
            quantity = int(self.quantity_input.text())
            if quantity <= 0:
                raise ValueError("Quantity must be positive")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid quantity")
            return

        if symbol not in self.portfolio:
            QMessageBox.warning(self, "Error", "You don't own this stock")
            return

        if quantity > self.portfolio[symbol]['shares']:
            QMessageBox.warning(self, "Error", "Insufficient shares")
            return

        sale_price = quantity * self.stock_prices[symbol]
        self.cash_balance += sale_price

        remaining_shares = self.portfolio[symbol]['shares'] - quantity
        if remaining_shares == 0:
            del self.portfolio[symbol]
        else:
            self.portfolio[symbol]['shares'] = remaining_shares

        self.update_portfolio_table()
        self.symbol_input.clear()
        self.quantity_input.clear()

def main():
    app = QApplication(sys.argv)
    simulator = StockMarketSimulator()
    simulator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
