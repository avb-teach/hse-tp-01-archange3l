# Проект: ТЗ1 — collect_files.sh  
### Автор: Шумилов Юрий Леонидович, группа ББИ2410

---

## Описание

Скрипт `collect_files.sh` предназначен для сбора всех файлов из входной директории (и всех её вложенных папок на любую глубину) в выходную директорию без вложенности.

Поддерживается опциональный параметр `--max_depth`, ограничивающий глубину обхода. При превышении указанной глубины, структура сохраняется с уровня, при котором глубина становится допустимой.

Скрипт написан с использованием Python и запускается через Bash. Поддерживаются Windows, Linux и системы автоматической проверки (CI).

---

## Как запустить

Перед использованием убедитесь, что в системе установлен Python 3.  
Скрипт `collect_files.sh` автоматически определяет операционную систему:

- В Git Bash на Windows используется `winpty python`
- В Linux / Mac / WSL / GitHub Actions — `python3`

Дополнительных действий от пользователя не требуется.

### Команда:

```bash
bash collect_files.sh input_dir output_dir [--max_depth N]
input_dir — путь к папке, откуда нужно собрать файлы

output_dir — путь к папке, куда поместятся файлы

--max_depth N — опциональный параметр, ограничивает глубину обхода (например, 3)
```
## Аргументы командной строки и примеры

```bash
# Общий формат запуска:
./collect_files.sh input_dir output_dir [--max_depth N]

# Примеры:
./collect_files.sh ./input ./output
./collect_files.sh ./input ./output --max_depth 3

# Пояснение параметров:
# input_dir     — путь к папке, откуда нужно собрать файлы
# output_dir    — путь к папке, куда поместятся файлы
# --max_depth N — (опционально) ограничивает глубину обхода (например, 3)
```
## Что реализовано
- Принимаются два обязательных параметра.

- Корректно обрабатывается любая вложенность.

- Разрешаются конфликты одинаковых имён (добавляются суффиксы: file1.txt, file2.txt и т.д.).

- Поддерживается параметр --max_depth.

- Кроссплатформенность: collect_files.sh работает как в Windows (через Git Bash), так и в Linux.

- Для Windows требуется запуск через winpty python collect_files.py ...
Для Linux — обычный вызов python3 collect_files.py ...

## Примеры

### Пример 1. Вложенность до 2 уровней

вход:
```css
input_dir/
├── a.txt
├── dir1/
│   └── b.txt
├── dir2/
│   └── c.txt
```
запуск:
```bash
bash collect_files.sh input_dir output_dir
```

результат:
```css
output_dir/
├── a.txt
├── b.txt
└── c.txt
```

### Пример 2. Конфликт имён

вход:
```css
input_dir/
├── file.txt
├── dir1/
│   └── file.txt
└── dir2/
    └── file.txt

```
запуск:
```bash
bash collect_files.sh input_dir output_dir
```

результат:
```css
output_dir/
├── file.txt
├── file1.txt
└── file2.txt
```

### Пример 3. Ограничение глубины --max_depth 2

вход:
```css
input_dir/
├── 1.txt
├── level2/
│   ├── 2.txt
│   └── level3/
│       ├── 3.txt
│       └── level4/
│           └── 4.txt
```
запуск:
```bash
bash collect_files.sh input_dir output_dir --max_depth 2
```

результат:
```css
output_dir/
├── 1.txt
└── 2.txt
```

### Пример 4. Без ограничения глубины

вход:
```css
input_dir/
└── a/
    └── b/
        └── c/
            └── d/
                └── deep.txt
```
запуск:
```bash
bash collect_files.sh input_dir output_dir
```

результат:
```css
output_dir/
└── deep.txt
```

