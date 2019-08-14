<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/env-strip.svg?maxAge=3600)](https://pypi.org/project/env-strip/)
[![](https://img.shields.io/npm/v/env-strip.svg?maxAge=3600)](https://www.npmjs.com/package/env-strip)
[![Travis](https://api.travis-ci.org/andrewp-as-is/env-strip.svg?branch=master)](https://travis-ci.org/andrewp-as-is/env-strip/)

#### Installation
```bash
$ [sudo] npm i -g env-strip
```
```bash
$ [sudo] pip install env-strip
```

#### Pros
+   Docker compatible environment file without comments, blank lines and double quotes

#### Scripts usage
command|`usage`
-|-
`env-strip` |`usage: env-strip path`

#### Examples
`.env`
```bash
SECRET_KEY="https://www.youtube.com/channel/UCTZUTvv_1Onm-f-533Hyurw"

# postgres settings:
DB_NAME="name" # comment
DB_USER="postgres" # comment
DB_HOST="127.0.0.1" # comment
DB_PORT=5432 # comment
```

```bash
$ env-strip .env
SECRET_KEY=https://www.youtube.com/channel/UCTZUTvv_1Onm-f-533Hyurw
DB_NAME=name
DB_USER=postgres
DB_HOST=127.0.0.1
DB_PORT=5432
```

stdin
```bash
$ find . \( -name .env.base -o -name ".env.prod.*" \) -exec cat {} \; | env-strip - > .env.prod
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>