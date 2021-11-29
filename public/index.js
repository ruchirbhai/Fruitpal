const sio = io();

sio.on('connect', () => {
  console.log('connected');
  data = {'commodity': 'mango', 'price_per_trade': '100', 'volume_in_tons': '1'}
  sio.emit('priceAPI',data)
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('sum_result', (data)=> {
    console.log(data)
})