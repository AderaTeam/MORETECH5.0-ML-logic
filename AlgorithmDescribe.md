# Как работает алгоритм

```mermaid
flowchart LR
    A1[Получение данных об окружении, погоде и т.д] --> B[Образование векторов состояний]
    A2[Получение данных о пользователе] --> B[Образование векторов состояний]
    A3[Получение данных об N отделениях] --> B[Образование N векторов состояний]
    B[Образование N векторов состояний] --> C[Каждый маршрут подаётся в среду Env]
    C[Обучение модели Mod в среде Env] --> D[Вывод валидности отделения/банкомата]
```

# Описание сущностей
- Env - среда с вероятностным распределением принять то или иное решение;
- Mod - лёгкая модель, для быстрого обучение в среде;
- Вектор состояний - описан в ноутбуке create_env.ipynb

# Описание среды Env
```mermaid
    classDiagram
        direction LR
        class Env{
            -callable get_propability_for_checkout_transport
            -callable change_distance_by_transport
            -callable get_propability_of_walk_age
            -callable propability_of_checkout_branch_by_raiting
            +step(dict state)
        }
```

# P.S.
Крч. очень хитро модефицированный алгоритм отжига.