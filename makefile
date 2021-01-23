GREEN=\n\033[1;32;40m
RED=\n\033[1;31;40m
NC=\033[0m # No Color

PYCODESTYLE = pycodestyle
MYPY = mypy
# no-member: mypy
PYLINTFLAGS = --verbose --reports=no --output-format=colorized --errors-only --disable=no-member --enable=unused-import

PYTHONFILES := $(shell find . -name '*.py' | grep -v .venv)
PYTHON_VERSION = py38
PYTHON_LINE_LENGTH = 80
targets:
	@echo $(PYTHONFILES)
.PHONY: targets

PIP := $(shell command -v pip 2> /dev/null)
PIPENV := $(shell command -v pipenv 2> /dev/null)

ref:
ifndef PIP
	# https://pip.pypa.io/en/stable/installing/
	$(error "pip이 설치되어 있지 않습니다.")
endif
	@/bin/sh -c "echo \"${GREEN}pip 설치되어 있음${NC}\""

ifndef PIPENV
	pip install pipenv
endif
	@/bin/sh -c "echo \"${GREEN}pipenv 설치되어 있음${NC}\""

.PHONY: ref

# 의존성 모듈 관리
venv_dir=.venv
venv-dev: 
ifneq "$(wildcard $(venv_dir) )" ""
	@/bin/sh -c "echo \"${GREEN}Already installation${NC}\""
else
	@/bin/sh -c "echo \"${GREEN}pipenv install${NC}\""
	export PIPENV_VENV_IN_PROJECT=${PWD} && pipenv install --dev
	pipenv graph
endif
.PHONY: venv-dev

pycodestyle: ref venv-dev
	@/bin/sh -c "echo \"${GREEN}[pycodestyle 시작]${NC}\""
	pipenv run $(PYCODESTYLE) --first $(PYTHONFILES)
.PHONY: pycodestyle

# vscode의 formatting 도구로 black을 사용
black: ref venv-dev
	@/bin/sh -c "echo \"${GREEN}[black 시작]${NC}\""
	pipenv run black -t $(PYTHON_VERSION) -l $(PYTHON_LINE_LENGTH) $(PYTHONFILES)
.PHONY: black

mypy: ref venv-dev
	@/bin/sh -c "echo \"${GREEN}[정적분석 시작]${NC}\""
	pipenv run $(MYPY) --config-file mypy.ini $(PYTHONFILES)
.PHONY: mypy

lint: pycodestyle mypy black
.PHONY: lint

test: ref venv-dev
	pipenv run pytest \
	--pdb \
	--cov=src tests \
	--cov-report=html \
	--cov-report=term \
	--cov-report=xml \
	--disable-warnings
.PHONY: test-coverage

requirements: ref venv-dev
	@/bin/sh -c "echo \"${GREEN}[requirements.txt를 추출합니다]${NC}\""
	@pipenv lock -r > requirements.txt
.PHONY: requirements

# 마지막 tag로부터 현재까지의 changelog 및 버전 확인 용
current_changelog:
	@/bin/sh -c "echo \"${GREEN}[release version] $(shell npx standard-version --dry-run | grep tagging | cut -d ' ' -f4)${NC}\""
	@/bin/sh -c "echo \"${GREEN}[description] ${NC}\""
	@npx standard-version --dry-run --silent | grep -v Done | grep -v "\-\-\-" | grep -v standard-version
.PHONY: current_changelog
