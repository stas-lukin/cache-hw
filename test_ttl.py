import memcache
import time

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

# Очищаем кеш
mc.flush_all()

print("=" * 55)
print("Задание 3: Тест TTL (Time To Live) в Memcached")
print("=" * 55)

# Записываем ключи с TTL 5 секунд
print("\n1. Записываем 3 ключа с TTL = 5 секунд:")
mc.set("color", "red", time=5)
mc.set("fruit", "apple", time=5)
mc.set("number", 100, time=5)
print("   → color = 'red'")
print("   → fruit = 'apple'")
print("   → number = 100")

# Проверяем что ключи есть
print("\n2. Проверяем сразу после записи:")
print(f"   color = {mc.get('color')}")
print(f"   fruit = {mc.get('fruit')}")
print(f"   number = {mc.get('number')}")

# Ждем 6 секунд
print("\n3. Ждем 6 секунд (TTL = 5 сек)...")
for i in range(6, 0, -1):
    print(f"   Осталось {i} сек", end="\r")
    time.sleep(1)

# Проверяем снова
print("\n\n4. Проверяем после ожидания:")
print(f"   color = {mc.get('color')}")
print(f"   fruit = {mc.get('fruit')}")
print(f"   number = {mc.get('number')}")

# Результат
print("\n" + "=" * 55)
if mc.get('color') is None and mc.get('fruit') is None and mc.get('number') is None:
    print("✅ РЕЗУЛЬТАТ: Все ключи успешно удалены по TTL!")
else:
    print("❌ РЕЗУЛЬТАТ: Не все ключи удалились")
print("=" * 55)
