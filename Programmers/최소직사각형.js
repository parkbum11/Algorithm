function solution(sizes) {
  let w_max = 0;
  let h_max = 0;
  sizes.forEach(element => {
    let w = 0;
    let h = 0;
    if (element[0] >= element[1]) {
      h = element[0];
      w = element[1];
    } else {
      h = element[1];
      w = element[0];
    }
    w_max = Math.max(w, w_max)
    h_max = Math.max(h, h_max)
  });
  return w_max * h_max;
}

solution([[60, 50], [30, 70], [60, 30], [80, 40]])