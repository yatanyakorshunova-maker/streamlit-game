import streamlit as st
import random

# --- 1. Заголовок и описание игры ---
st.set_page_config(page_title="🎯 Угадай число!", page_icon="🎲")
st.title("🎯 Угадай число от 1 до 100")
st.write("Попробуй угадать число, которое загадал компьютер. Это твой сайт!")

# --- 2. Состояние игры (секретное число) ---
# 'session_state' нужен, чтобы данные не сбрасывались при каждом нажатии кнопки [citation:2][citation:6]
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.feedback = "🤔 Введи число и нажми 'Проверить'."

# --- 3. Интерфейс для ввода и кнопки ---
user_guess = st.number_input(
    "Твой вариант:",
    min_value=1,
    max_value=100,
    step=1,
    key="guess_input",
    help="Введи число от 1 до 100"
)

col1, col2, col3 = st.columns(3)
with col1:
    check_button = st.button("✅ Проверить")
with col2:
    new_game_button = st.button("🔄 Новая игра")
with col3:
    hint_button = st.button("💡 Подсказка")

# --- 4. Игровая логика ---

# Логика кнопки "Проверить"
if check_button:
    st.session_state.attempts += 1
    if user_guess < st.session_state.secret_number:
        st.session_state.feedback = f"📈 Загаданное число **больше**, чем {user_guess}. Попробуй еще!"
    elif user_guess > st.session_state.secret_number:
        st.session_state.feedback = f"📉 Загаданное число **меньше**, чем {user_guess}. Попробуй еще!"
    else:
        st.session_state.feedback = f"🎉 **Поздравляю!** Ты угадал число {st.session_state.secret_number} за {st.session_state.attempts} попыток!"
        # Можно добавить красивый эффект при победе
        st.balloons()

# Логика кнопки "Новая игра"
if new_game_button:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.feedback = "🆕 Новая игра! Загадано новое число."

# Логика кнопки "Подсказка"
if hint_button:
    if user_guess < st.session_state.secret_number:
        st.session_state.feedback = f"💡 Подсказка: загаданное число больше, чем {user_guess}."
    elif user_guess > st.session_state.secret_number:
        st.session_state.feedback = f"💡 Подсказка: загаданное число меньше, чем {user_guess}."
    else:
        st.session_state.feedback = f"😉 Ты уже угадал! Зачем тебе подсказка?"

# --- 5. Отображение информации для игрока ---
st.divider()
st.markdown(f"### {st.session_state.feedback}")
st.metric(label="Количество попыток", value=st.session_state.attempts)
st.caption("💡 Это игра работает прямо в твоем браузере, потому что ты используешь Streamlit!")

# --- 6. Бонус: показать секретное число (для отладки или родителей) ---
with st.expander("👀 Секретная информация (для взрослых)"):
    st.write(f"Загаданное число: **{st.session_state.secret_number}**")
