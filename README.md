# Stdout Forwarding

python에서 stdout에 출력되는 메세지를 stdout과 로그파일에 동시에 출력하기 위한 모듈입니다.

## Usage

```python
import stdoutforwarding as forwarding

forwarding.start('out.log')
print('This message will be printed in both sys.stdout and out.log.')

forwarding.stop()
print('This message will be printed only in sys.stdout.')
```
