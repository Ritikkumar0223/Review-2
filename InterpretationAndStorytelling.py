import React, { useState, useEffect } from 'react';
import { LineChart, Line, AreaChart, Area, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell, ScatterPlot, Scatter } from 'recharts';
import { TrendingUp, TrendingDown, DollarSign, Activity, BarChart3, Filter, RefreshCw } from 'lucide-react';

const StockMarketDashboard = () => {
  const [selectedStock, setSelectedStock] = useState('AAPL');
  const [timeframe, setTimeframe] = useState('1M');
  const [viewType, setViewType] = useState('price');
  const [hoveredData, setHoveredData] = useState(null);
  const [animationKey, setAnimationKey] = useState(0);

  // Mock stock data - in real app, this would come from an API
  const stockData = {
    'AAPL': {
      name: 'Apple Inc.',
      current: 185.42,
      change: 2.34,
      changePercent: 1.28,
      volume: 45623000,
      marketCap: 2890000000000,
      priceHistory: [
        { date: '2024-01-01', price: 180.25, volume: 52000000, high: 182.5, low: 178.3, open: 179.1, close: 180.25 },
        { date: '2024-01-02', price: 182.15, volume: 48000000, high: 184.2, low: 180.8, open: 180.25, close: 182.15 },
        { date: '2024-01-03', price: 178.90, volume: 61000000, high: 183.1, low: 177.5, open: 182.15, close: 178.90 },
        { date: '2024-01-04', price: 181.75, volume: 43000000, high: 183.8, low: 179.2, open: 178.90, close: 181.75 },
        { date: '2024-01-05', price: 185.42, volume: 45623000, high: 186.9, low: 182.1, open: 181.75, close: 185.42 },
      ]
    },
    'GOOGL': {
      name: 'Alphabet Inc.',
      current: 142.68,
      change: -1.87,
      changePercent: -1.29,
      volume: 23450000,
      marketCap: 1780000000000,
      priceHistory: [
        { date: '2024-01-01', price: 145.20, volume: 28000000, high: 147.1, low: 143.8, open: 144.5, close: 145.20 },
        { date: '2024-01-02', price: 143.85, volume: 31000000, high: 146.2, low: 142.9, open: 145.20, close: 143.85 },
        { date: '2024-01-03', price: 147.30, volume: 25000000, high: 148.5, low: 144.1, open: 143.85, close: 147.30 },
        { date: '2024-01-04', price: 144.55, volume: 29000000, high: 148.0, low: 143.2, open: 147.30, close: 144.55 },
        { date: '2024-01-05', price: 142.68, volume: 23450000, high: 145.8, low: 141.9, open: 144.55, close: 142.68 },
      ]
    },
    'TSLA': {
      name: 'Tesla Inc.',
      current: 248.91,
      change: 8.45,
      changePercent: 3.51,
      volume: 89234000,
      marketCap: 790000000000,
      priceHistory: [
        { date: '2024-01-01', price: 235.20, volume: 95000000, high: 238.5, low: 232.1, open: 234.0, close: 235.20 },
        { date: '2024-01-02', price: 240.75, volume: 78000000, high: 243.2, low: 236.8, open: 235.20, close: 240.75 },
        { date: '2024-01-03', price: 238.46, volume: 102000000, high: 242.9, low: 235.3, open: 240.75, close: 238.46 },
        { date: '2024-01-04', price: 245.33, volume: 84000000, high: 248.1, low: 239.7, open: 238.46, close: 245.33 },
        { date: '2024-01-05', price: 248.91, volume: 89234000, high: 251.8, low: 246.2, open: 245.33, close: 248.91 },
      ]
    }
  };

  // Portfolio allocation data
  const portfolioData = [
    { name: 'Technology', value: 45, color: '#3B82F6' },
    { name: 'Healthcare', value: 20, color: '#10B981' },
    { name: 'Finance', value: 15, color: '#F59E0B' },
    { name: 'Energy', value: 12, color: '#EF4444' },
    { name: 'Consumer', value: 8, color: '#8B5CF6' }
  ];

  // Volume vs Price correlation data
  const correlationData = stockData[selectedStock].priceHistory.map(item => ({
    volume: item.volume / 1000000, // Convert to millions
    price: item.price,
    date: item.date
  }));

  const currentStock = stockData[selectedStock];

  // Interactive handlers
  const handleStockChange = (stock) => {
    setSelectedStock(stock);
    setAnimationKey(prev => prev + 1);
  };

  const handleTimeframeChange = (tf) => {
    setTimeframe(tf);
    setAnimationKey(prev => prev + 1);
  };

  const refreshData = () => {
    setAnimationKey(prev => prev + 1);
  };

  // Custom tooltip components
  const CustomTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white p-3 border border-gray-300 rounded-lg shadow-lg">
          <p className="font-semibold">{`Date: ${label}`}</p>
          {payload.map((entry, index) => (
            <p key={index} style={{ color: entry.color }}>
              {`${entry.dataKey}: $${entry.value.toFixed(2)}`}
            </p>
          ))}
        </div>
      );
    }
    return null;
  };

  const VolumeTooltip = ({ active, payload, label }) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white p-3 border border-gray-300 rounded-lg shadow-lg">
          <p className="font-semibold">{`Date: ${label}`}</p>
          <p style={{ color: payload[0].color }}>
            {`Volume: ${(payload[0].value * 1000000).toLocaleString()}`}
          </p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-xl shadow-lg p-6 mb-8">
          <div className="flex justify-between items-center mb-6">
            <h1 className="text-3xl font-bold text-gray-800">Stock Market Analysis Dashboard</h1>
            <button 
              onClick={refreshData}
              className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors"
            >
              <RefreshCw size={18} />
              Refresh Data
            </button>
          </div>
          
          {/* Interactive Controls */}
          <div className="flex flex-wrap gap-4 mb-6">
            <div className="flex items-center gap-2">
              <Filter size={18} className="text-gray-600" />
              <span className="font-medium">Stock:</span>
              <select 
                value={selectedStock} 
                onChange={(e) => handleStockChange(e.target.value)}
                className="border border-gray-300 rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
                <option value="AAPL">Apple (AAPL)</option>
                <option value="GOOGL">Alphabet (GOOGL)</option>
                <option value="TSLA">Tesla (TSLA)</option>
              </select>
            </div>
            
            <div className="flex items-center gap-2">
              <span className="font-medium">Timeframe:</span>
              {['1W', '1M', '3M', '1Y'].map(tf => (
                <button
                  key={tf}
                  onClick={() => handleTimeframeChange(tf)}
                  className={`px-3 py-2 rounded-lg transition-colors ${
                    timeframe === tf 
                      ? 'bg-blue-600 text-white' 
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  {tf}
                </button>
              ))}
            </div>

            <div className="flex items-center gap-2">
              <span className="font-medium">View:</span>
              {[
                { key: 'price', label: 'Price', icon: TrendingUp },
                { key: 'volume', label: 'Volume', icon: BarChart3 },
                { key: 'correlation', label: 'Correlation', icon: Activity }
              ].map(({ key, label, icon: Icon }) => (
                <button
                  key={key}
                  onClick={() => setViewType(key)}
                  className={`flex items-center gap-1 px-3 py-2 rounded-lg transition-colors ${
                    viewType === key 
                      ? 'bg-green-600 text-white' 
                      : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                  }`}
                >
                  <Icon size={16} />
                  {label}
                </button>
              ))}
            </div>
          </div>

          {/* Stock Summary Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div className="bg-gradient-to-r from-blue-500 to-blue-600 text-white p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-blue-100 text-sm">Current Price</p>
                  <p className="text-2xl font-bold">${currentStock.current}</p>
                </div>
                <DollarSign size={32} className="text-blue-200" />
              </div>
            </div>
            
            <div className={`${currentStock.change >= 0 ? 'bg-gradient-to-r from-green-500 to-green-600' : 'bg-gradient-to-r from-red-500 to-red-600'} text-white p-4 rounded-lg`}>
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-white text-opacity-80 text-sm">Daily Change</p>
                  <p className="text-2xl font-bold">{currentStock.change >= 0 ? '+' : ''}${currentStock.change}</p>
                  <p className="text-sm">({currentStock.changePercent >= 0 ? '+' : ''}{currentStock.changePercent}%)</p>
                </div>
                {currentStock.change >= 0 ? <TrendingUp size={32} /> : <TrendingDown size={32} />}
              </div>
            </div>
            
            <div className="bg-gradient-to-r from-purple-500 to-purple-600 text-white p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-purple-100 text-sm">Volume</p>
                  <p className="text-2xl font-bold">{(currentStock.volume / 1000000).toFixed(1)}M</p>
                </div>
                <Activity size={32} className="text-purple-200" />
              </div>
            </div>
            
            <div className="bg-gradient-to-r from-orange-500 to-orange-600 text-white p-4 rounded-lg">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-orange-100 text-sm">Market Cap</p>
                  <p className="text-2xl font-bold">${(currentStock.marketCap / 1000000000000).toFixed(2)}T</p>
                </div>
                <BarChart3 size={32} className="text-orange-200" />
              </div>
            </div>
          </div>
        </div>

        {/* Main Charts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
          {/* Price Chart */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4">
              {currentStock.name} - Price Movement
            </h2>
            <ResponsiveContainer width="100%" height={300}>
              <AreaChart data={currentStock.priceHistory} key={`price-${animationKey}`}>
                <defs>
                  <linearGradient id="colorPrice" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#3B82F6" stopOpacity={0.1}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
                <XAxis 
                  dataKey="date" 
                  stroke="#6B7280"
                  fontSize={12}
                  tickFormatter={(value) => new Date(value).toLocaleDateString()}
                />
                <YAxis 
                  stroke="#6B7280"
                  fontSize={12}
                  tickFormatter={(value) => `$${value}`}
                />
                <Tooltip content={<CustomTooltip />} />
                <Area
                  type="monotone"
                  dataKey="price"
                  stroke="#3B82F6"
                  strokeWidth={3}
                  fillOpacity={1}
                  fill="url(#colorPrice)"
                  animationDuration={1500}
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          {/* Volume Chart */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4">Trading Volume</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={currentStock.priceHistory} key={`volume-${animationKey}`}>
                <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
                <XAxis 
                  dataKey="date" 
                  stroke="#6B7280"
                  fontSize={12}
                  tickFormatter={(value) => new Date(value).toLocaleDateString()}
                />
                <YAxis 
                  stroke="#6B7280"
                  fontSize={12}
                  tickFormatter={(value) => `${(value / 1000000).toFixed(0)}M`}
                />
                <Tooltip content={<VolumeTooltip />} />
                <Bar 
                  dataKey="volume" 
                  fill="#10B981"
                  radius={[4, 4, 0, 0]}
                  animationDuration={1500}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Secondary Charts */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Price vs Volume Correlation */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4">Price vs Volume Analysis</h2>
            <ResponsiveContainer width="100%" height={300}>
              <ScatterPlot data={correlationData} key={`scatter-${animationKey}`}>
                <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
                <XAxis 
                  type="number" 
                  dataKey="volume" 
                  name="Volume"
                  stroke="#6B7280"
                  fontSize={12}
                  tickFormatter={(value) => `${value.toFixed(0)}M`}
                />
                <YAxis 
                  type="number" 
                  dataKey="price" 
                  name="Price"
                  stroke="#6B7280"
                  fontSize={12}
                  tickFormatter={(value) => `$${value}`}
                />
                <Tooltip 
                  cursor={{ strokeDasharray: '3 3' }}
                  formatter={(value, name) => [
                    name === 'volume' ? `${value.toFixed(1)}M` : `$${value.toFixed(2)}`,
                    name === 'volume' ? 'Volume' : 'Price'
                  ]}
                />
                <Scatter 
                  dataKey="price" 
                  fill="#8B5CF6"
                  animationDuration={1500}
                />
              </ScatterPlot>
            </ResponsiveContainer>
          </div>

          {/* Portfolio Allocation */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h2 className="text-xl font-bold text-gray-800 mb-4">Portfolio Allocation</h2>
            <ResponsiveContainer width="100%" height={300}>
              <PieChart key={`pie-${animationKey}`}>
                <Pie
                  data={portfolioData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                  animationDuration={1500}
                >
                  {portfolioData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip 
                  formatter={(value) => [`${value}%`, 'Allocation']}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Enhanced Data Storytelling Section */}
        <div className="bg-white rounded-xl shadow-lg p-6 mt-8">
          <h2 className="text-xl font-bold text-gray-800 mb-6">📊 Data Story: What the Numbers Tell Us</h2>
          
          {/* Key Performance Narrative */}
          <div className="bg-gradient-to-r from-slate-50 to-blue-50 p-6 rounded-lg mb-6">
            <h3 className="text-lg font-bold text-gray-800 mb-3">🎯 Performance Narrative</h3>
            <div className="prose text-gray-700">
              <p className="mb-3">
                <strong>Market Story:</strong> {currentStock.name} is currently trading at <span className="font-bold text-blue-600">${currentStock.current}</span>, 
                {currentStock.change >= 0 
                  ? ` showing bullish momentum with a ${currentStock.changePercent}% gain (+${currentStock.change}). This upward trajectory suggests strong investor confidence and potential continued growth.`
                  : ` facing bearish pressure with a ${Math.abs(currentStock.changePercent)}% decline (-${Math.abs(currentStock.change)}). This dip could represent a strategic entry point for value-oriented investors.`
                }
              </p>
              
              <p className="mb-3">
                <strong>Volume Intelligence:</strong> Today's trading volume of <span className="font-bold text-green-600">{(currentStock.volume / 1000000).toFixed(1)}M shares</span>
                {currentStock.volume > 70000000 
                  ? " indicates exceptional market interest - nearly double the typical volume. This surge suggests significant news or institutional activity driving price action."
                  : currentStock.volume > 40000000
                  ? " represents above-average market participation, signaling heightened investor attention and potential volatility ahead."
                  : " shows steady, controlled trading conditions with balanced buyer-seller dynamics typical of stable market periods."
                }
              </p>
              
              <p>
                <strong>Market Context:</strong> With a market capitalization of <span className="font-bold text-purple-600">${(currentStock.marketCap / 1000000000000).toFixed(2)}T</span>, 
                {currentStock.marketCap > 2000000000000 
                  ? " this stock commands significant market influence as a mega-cap leader, often serving as a market bellwether."
                  : currentStock.marketCap > 1000000000000
                  ? " this represents a large-cap stalwart with substantial institutional ownership and lower volatility profile."
                  : " this mid-to-large cap position offers growth potential while maintaining relative stability."
                }
              </p>
            </div>
          </div>

          {/* Technical Analysis Story */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <div className="bg-gradient-to-br from-blue-50 to-indigo-100 p-5 rounded-lg">
              <h3 className="font-bold text-blue-800 mb-3 flex items-center gap-2">
                <TrendingUp size={20} />
                📈 Price Action Analysis
              </h3>
              <div className="space-y-2 text-sm text-blue-800">
                {(() => {
                  const prices = currentStock.priceHistory.map(d => d.price);
                  const trend = prices[prices.length - 1] > prices[0] ? 'upward' : 'downward';
                  const volatility = Math.max(...prices) - Math.min(...prices);
                  const avgPrice = prices.reduce((a, b) => a + b) / prices.length;
                  
                  return (
                    <>
                      <p><strong>5-Day Trend:</strong> {trend === 'upward' ? '📈 Bullish' : '📉 Bearish'} ({((prices[prices.length - 1] / prices[0] - 1) * 100).toFixed(1)}% net change)</p>
                      <p><strong>Volatility Range:</strong> ${volatility.toFixed(2)} ({((volatility / avgPrice) * 100).toFixed(1)}% of average price)</p>
                      <p><strong>Price Position:</strong> Currently {currentStock.current > avgPrice ? '🔴 above' : '🟢 below'} 5-day average (${avgPrice.toFixed(2)})</p>
                      <p><strong>Momentum Signal:</strong> {currentStock.changePercent > 2 ? '🚀 Strong bullish' : currentStock.changePercent > 0 ? '📈 Mild bullish' : currentStock.changePercent > -2 ? '📉 Mild bearish' : '⚠️ Strong bearish'}</p>
                    </>
                  );
                })()}
              </div>
            </div>

            <div className="bg-gradient-to-br from-green-50 to-emerald-100 p-5 rounded-lg">
              <h3 className="font-bold text-green-800 mb-3 flex items-center gap-2">
                <Activity size={20} />
                📊 Volume & Liquidity Story
              </h3>
              <div className="space-y-2 text-sm text-green-800">
                {(() => {
                  const volumes = currentStock.priceHistory.map(d => d.volume);
                  const avgVolume = volumes.reduce((a, b) => a + b) / volumes.length;
                  const volumeRatio = currentStock.volume / avgVolume;
                  
                  return (
                    <>
                      <p><strong>Volume Trend:</strong> {volumeRatio > 1.5 ? '🔥 Exceptionally high' : volumeRatio > 1.2 ? '📈 Above average' : volumeRatio > 0.8 ? '➡️ Normal range' : '📉 Below average'}</p>
                      <p><strong>5-Day Avg Volume:</strong> {(avgVolume / 1000000).toFixed(1)}M shares</p>
                      <p><strong>Today vs Average:</strong> {(volumeRatio * 100).toFixed(0)}% of typical volume</p>
                      <p><strong>Liquidity Status:</strong> {currentStock.volume > 50000000 ? '💧 Highly liquid' : '🌊 Moderately liquid'} - {currentStock.volume > 50000000 ? 'Easy' : 'Standard'} entry/exit</p>
                    </>
                  );
                })()}
              </div>
            </div>
          </div>

          {/* Predictive Insights */}
          <div className="bg-gradient-to-r from-amber-50 to-orange-100 p-6 rounded-lg mb-6">
            <h3 className="text-lg font-bold text-amber-800 mb-3 flex items-center gap-2">
              🔮 Predictive Insights & Market Signals
            </h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <h4 className="font-semibold text-amber-800 mb-2">📊 Technical Indicators Suggest:</h4>
                <ul className="text-sm text-amber-700 space-y-1">
                  {currentStock.changePercent > 2 ? (
                    <>
                      <li>• 🎯 Strong momentum may continue short-term</li>
                      <li>• ⚠️ Watch for profit-taking at resistance levels</li>
                      <li>• 📈 Consider position sizing on pullbacks</li>
                    </>
                  ) : currentStock.changePercent > 0 ? (
                    <>
                      <li>• 📈 Modest uptrend with room for growth</li>
                      <li>• ✅ Stable foundation for continued gains</li>
                      <li>• 🎯 Monitor volume for confirmation</li>
                    </>
                  ) : (
                    <>
                      <li>• 📉 Potential oversold conditions emerging</li>
                      <li>• 💡 Value opportunity for patient investors</li>
                      <li>• 🔍 Watch for reversal signals</li>
                    </>
                  )}
                </ul>
              </div>
              <div>
                <h4 className="font-semibold text-amber-800 mb-2">🎯 Risk-Reward Assessment:</h4>
                <div className="text-sm text-amber-700 space-y-1">
                  <p><strong>Risk Level:</strong> {
                    currentStock.volume > 80000000 ? '🔴 High (elevated volume suggests volatility)' :
                    Math.abs(currentStock.changePercent) > 3 ? '🟡 Moderate-High (significant price movement)' :
                    '🟢 Moderate (stable trading conditions)'
                  }</p>
                  <p><strong>Opportunity Score:</strong> {
                    currentStock.changePercent > 2 ? '📈 High (momentum play)' :
                    currentStock.changePercent < -2 ? '💎 High (value play)' :
                    '📊 Moderate (steady performer)'
                  }</p>
                  <p><strong>Time Horizon:</strong> {currentStock.volume > 60000000 ? 'Short-term focus' : 'Medium-term hold'} recommended</p>
                </div>
              </div>
            </div>
          </div>

          {/* Comparative Analysis */}
          <div className="bg-gradient-to-r from-purple-50 to-pink-100 p-6 rounded-lg">
            <h3 className="text-lg font-bold text-purple-800 mb-3">🏆 Comparative Market Analysis</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {Object.entries(stockData).map(([symbol, data]) => (
                <div key={symbol} className={`p-4 rounded-lg border-2 ${selectedStock === symbol ? 'border-purple-400 bg-purple-100' : 'border-purple-200 bg-white'}`}>
                  <div className="flex justify-between items-center mb-2">
                    <h4 className="font-bold text-purple-800">{symbol}</h4>
                    <span className={`text-sm font-semibold ${data.change >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                      {data.change >= 0 ? '+' : ''}{data.changePercent}%
                    </span>
                  </div>
                  <p className="text-sm text-purple-700 mb-1">${data.current}</p>
                  <div className="text-xs text-purple-600">
                    <p>Vol: {(data.volume / 1000000).toFixed(1)}M</p>
                    <p>Cap: ${(data.marketCap / 1000000000000).toFixed(2)}T</p>
                  </div>
                  {selectedStock === symbol && (
                    <div className="mt-2 text-xs text-purple-800 font-medium">
                      👑 Currently Analyzing
                    </div>
                  )}
                </div>
              ))}
            </div>
            <div className="mt-4 p-4 bg-white rounded-lg">
              <p className="text-sm text-purple-700">
                <strong>Cross-Stock Insight:</strong> {
                  (() => {
                    const allStocks = Object.values(stockData);
                    const avgChange = allStocks.reduce((sum, stock) => sum + stock.changePercent, 0) / allStocks.length;
                    const currentPerformance = currentStock.changePercent;
                    
                    if (currentPerformance > avgChange + 1) {
                      return `${currentStock.name} is significantly outperforming the tracked portfolio today, suggesting company-specific positive catalysts or sector strength.`;
                    } else if (currentPerformance < avgChange - 1) {
                      return `${currentStock.name} is underperforming relative to peers, which could indicate stock-specific headwinds or present a relative value opportunity.`;
                    } else {
                      return `${currentStock.name} is performing in line with the broader market trend, showing correlated movement with other major stocks.`;
                    }
                  })()
                }
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StockMarketDashboard;