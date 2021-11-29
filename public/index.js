const sio = io();

sio.on('connect', () => {
  console.log('connected');
  // Define Test for each type of commodity
  mangoTest = {'commodity': 'mango', 'price_per_trade': '100', 'volume_in_tons': '1'}
  appeleTest = {'commodity': 'apple', 'price_per_trade': '100', 'volume_in_tons': '1'}
  pineapple = {'commodity': 'pineapple', 'price_per_trade': '100', 'volume_in_tons': '1'}

  // Send test data to frutiServer for validation
  sio.emit('priceAPI',mangoTest)
  sio.emit('priceAPI',appeleTest)
  sio.emit('priceAPI',pineapple)

  // Wrong values
  // commodity value missing
  errorValTest1 = {'commodity': '', 'price_per_trade': '100', 'volume_in_tons': '1'}
  sio.emit('priceAPI',errorValTest1)
  // price_per_trade is not a number
  errorValTest2 = {'commodity': 'mango', 'price_per_trade': 'hundred', 'volume_in_tons': '1'}
  sio.emit('priceAPI',errorValTest2)
  //volume_in_tons
  errorValTest3 = {'commodity': 'mango', 'price_per_trade': '100', 'volume_in_tons': 'one'}
  sio.emit('priceAPI',errorValTest3)
});

sio.on('disconnect', () => {
  console.log('disconnected');
});

sio.on('sum_result', (data)=> {
    console.log(data)
})