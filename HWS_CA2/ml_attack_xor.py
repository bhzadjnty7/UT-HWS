import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# بارگذاری CRPهای ذخیره‌شده (که قبلاً توسط XORArbiterPUF تولید شده‌اند)
challenges = np.loadtxt("xor_challenges.csv", delimiter=",", dtype=int)
responses = np.loadtxt("xor_responses.csv", delimiter=",", dtype=int)

# تقسیم‌بندی داده‌ها به آموزش و آزمون (70% آموزش، 30% آزمون)
X_train, X_test, y_train, y_test = train_test_split(
    challenges, responses, test_size=0.3, random_state=42
)

# ساخت و آموزش مدل رگرسیون لجستیک
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# پیش‌بینی پاسخ‌های آزمون و محاسبه دقت
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("XOR Arbiter PUF - ML Attack Accuracy:", accuracy)

