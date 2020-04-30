# Stdout forwarding

python에서 stdout에 출력되는 모든 메세지를 지정된 파일에도 동시에 출력하기 위한 모듈입니다.

## Usage

```python
import stdoutforwarding as forwarding

forwarding.start('out.log')
print('This message will be printed in both stdout and out.log.')

forwarding.stop()
print('This message will be printed only in stdout.')
```
