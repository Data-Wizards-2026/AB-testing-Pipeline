# **Planned Folder structure**

```
AB_testing_Pipeline/
│
├── engine/
│   │
│   ├── __init__.py
│   │
│   ├── experiment.py
│   ├── assignment.py
│   ├── events.py
│   │
│   ├── metrics.py
│   ├── statistics.py
│   └── decision.py
│
├── data/
│   │
│   └── sample_data/
│
├── api/
│   │
│   ├── __init__.py
│   ├── main.py
│   └── routes/
│
├── database/
│   │
│   ├── __init__.py
│   ├── models.py
│   └── connection.py
│
├── cli/
│   │
│   └── main.py
│
├── tests/
│   │
│   ├── test_experiment.py
│   ├── test_assignment.py
│   ├── test_events.py
│   ├── test_metrics.py
│   ├── test_statistics.py
│   └── test_decision.py
│
├── requirements.txt
├── README.md
└── .gitignore
```