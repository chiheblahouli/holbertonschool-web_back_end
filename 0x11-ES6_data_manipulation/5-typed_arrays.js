export default function createInt8TypedArray(length, position, value) {
  try {
    const f = new DataView(new ArrayBuffer(length));
    f.setInt8(position, value);
    return f;
  } catch (e) {
    throw Error('Position outside range');
  }
}
