// 验证是否整数,非必填
export function isIntegerNotMust(rule, value, callback) {
    if (!value) {
      callback();
    }
    setTimeout(() => {
      if (!Number(value)) {
        callback(new Error('请输入数字'));
      } else {
        const re = /^[0-9]*[1-9][0-9]*$/;
        const rsCheck = re.test(value);
        if (!rsCheck) {
          callback(new Error('请输入数字'));
        } else {
          callback();
        }
      }
    }, 1000);
  }