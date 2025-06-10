import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area, BarChart, Bar, ScatterChart, Scatter, PieChart, Pie, Cell, CandlestickChart, RadialBarChart, RadialBar } from 'recharts';
import { TrendingUp, TrendingDown, BarChart3, PieChart, Activity, Zap } from 'lucide-react';

const ChartSelectionGuide = () => {
  const [activeChart, setActiveChart] = useState('line');

  // Sample data for different chart types
  const priceData = [
    { date: '2024-01', AAPL: 175.25, GOOGL: 142.56, TSLA: 248.42 },
    { date: '2024-02', AAPL: 181.86, GOOGL: 139.91, TSLA: 201.29 },
    { date: '2024-03', AAPL: 169.12, GOOGL: 141.75, TSLA: 175.79 },
    { date: '2024-04', AAPL: 185.43, GOOGL: 155.89, TSLA: 194.77 },
    { date: '2024-05', AAPL: 189.47, GOOGL: 138.21, TSLA: 234.86 }
  ];

  const candlestickData = [
    { date: '2024-01', open: 174.2, high: 180.1, low: 172.8, close: 175.25 },
    { date: '2024-02', open: 175.25, high: 185.4, low: 176.2, close: 181.86 },
    { date: '2024-03', open: 181.86, high: 182.9, low: 165.8, close: 169.12 },
    { date: '2024-04', open: 169.12, high: 188.7, low: 168.4, close: 185.43 },
    { date: '2024-05', open: 185.43, high: 192.1, low: 183.6, close: 189.47 }
  ];

  const volumeData = [
    { date: '2024-01', volume: 48.3, price: 175.25 },
    { date: '2024-02', volume: 52.1, price: 181.86 },
    { date: '2024-03', volume: 58.7, price: 169.12 },
    { date: '2024-04', volume: 51.2, price: 185.43 },
    { date: '2024-05', volume: 54.2, price: 189.47 }
  ];

  const sectorData = [
    { name: 'Technology', value: 28.5, color: '#3B82F6' },
    { name: 'Healthcare', value: 13.2, color: '#10B981' },
    { name: 'Financial', value: 11.8, color: '#F59E0B' },
    { name: 'Consumer', value: 10.9, color: '#EF4444' },
    { name: 'Energy', value: 8.4, color: '#8B5CF6' },
    { name: 'Others', value: 27.2, color: '#6B7280' }
  ];

  const correlationData = [
    { stock1: 175.25, stock2: 142.56, name: 'Jan' },
    { stock1: 181.86, stock2: 139.91, name: 'Feb' },
    { stock1: 169.12, stock2: 141.75, name: 'Mar' },
    { stock1: 185.43, stock2: 155.89, name: 'Apr' },
    { stock1: 189.47, stock2: 138.21, name: 'May' }
  ];

  const performanceData = [
    { stock: 'AAPL', performance: 8.1, fill: '#3B82F6' },
    { stock: 'GOOGL', performance: -2.9, fill: '#EF4444' },
    { stock: 'TSLA', performance: -5.4, fill: '#EF4444' },
    { stock: 'MSFT', performance: 12.3, fill: '#10B981' },
    { stock: 'AMZN', performance: 15.7, fill: '#10B981' }
  ];

  const volatilityData = [
    { date: '2024-01', volatility: 15.2 },
    { date: '2024-02', volatility: 22.8 },
    { date: '2024-03', volatility: 31.5 },
    { date: '2024-04', volatility: 18.9 },
    { date: '2024-05', volatility: 25.1 }
  ];

  const chartTypes = [
    {
      id: 'line',
      name: 'Line Chart',
      icon: <Activity className="w-5 h-5" />,
      purpose: 'Track price trends over time',
      bestFor: 'Continuous data, time series, trend analysis',
      insights: 'Price movements, trend direction, comparative performance'
    },
    {
      id: 'area',
      name: 'Area Chart',
      icon: <TrendingUp className="w-5 h-5" />,
      purpose: 'Emphasize magnitude of change',
      bestFor: 'Volume under curve, cumulative values',
      insights: 'Market momentum, volume trends, portfolio growth'
    },
    {
      id: 'candlestick',
      name: 'Candlestick Chart',
      icon: <BarChart3 className="w-5 h-5" />,
      purpose: 'Show OHLC data in single view',
      bestFor: 'Trading analysis, price action patterns',
      insights: 'Market sentiment, support/resistance, trading patterns'
    },
    {
      id: 'bar',
      name: 'Bar Chart',
      icon: <BarChart3 className="w-5 h-5" />,
      purpose: 'Compare discrete categories',
      bestFor: 'Performance comparison, rankings',
      insights: 'Stock performance, sector comparison, volume analysis'
    },
    {
      id: 'pie',
      name: 'Pie Chart',
      icon: <PieChart className="w-5 h-5" />,
      purpose: 'Show composition of whole',
      bestFor: 'Portfolio allocation, market share',
      insights: 'Asset allocation, sector distribution, market composition'
    },
    {
      id: 'scatter',
      name: 'Scatter Plot',
      icon: <Zap className="w-5 h-5" />,
      purpose: 'Show correlation between variables',
      bestFor: 'Risk vs return, correlation analysis',
      insights: 'Stock correlations, risk-return relationships, market efficiency'
    }
  ];

  const CustomCandlestick = ({ data }) => {
    return (
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
          <XAxis dataKey="date" stroke="#9CA3AF" />
          <YAxis stroke="#9CA3AF" />
          <Tooltip 
            content={({ active, payload, label }) => {
              if (active && payload && payload.length) {
                const data = payload[0].payload;
                return (
                  <div className="bg-gray-900 p-3 rounded-lg border border-gray-700">
                    <p className="text-gray-300">{label}</p>
                    <p className="text-white">Open: ${data.open}</p>
                    <p className="text-white">High: ${data.high}</p>
                    <p className="text-white">Low: ${data.low}</p>
                    <p className="text-white">Close: ${data.close}</p>
                  </div>
                );
              }
              return null;
            }}
          />
          {data.map((entry, index) => (
            <Bar 
              key={index} 
              x={index * 100} 
              width={20} 
              fill={entry.close > entry.open ? '#10B981' : '#EF4444'} 
            />
          ))}
        </BarChart>
      </ResponsiveContainer>
    );
  };

  const renderChart = () => {
    switch(activeChart) {
      case 'line':
        return (
          <div className="space-y-4">
            <div className="bg-blue-900/20 p-4 rounded-lg border border-blue-700">
              <h4 className="font-semibold text-blue-300 mb-2">Why Line Charts for Stock Prices?</h4>
              <p className="text-sm text-gray-300">
                Line charts excel at showing continuous data trends over time. They clearly display price movements, 
                making it easy to identify uptrends, downtrends, and sideways movements. Perfect for comparing multiple stocks.
              </p>
            </div>
            <ResponsiveContainer width="100%" height={400}>
              <LineChart data={priceData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="date" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }}
                  labelStyle={{ color: '#9CA3AF' }}
                />
                <Legend />
                <Line type="monotone" dataKey="AAPL" stroke="#3B82F6" strokeWidth={3} dot={{ r: 6 }} />
                <Line type="monotone" dataKey="GOOGL" stroke="#10B981" strokeWidth={3} dot={{ r: 6 }} />
                <Line type="monotone" dataKey="TSLA" stroke="#EF4444" strokeWidth={3} dot={{ r: 6 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        );

      case 'area':
        return (
          <div className="space-y-4">
            <div className="bg-green-900/20 p-4 rounded-lg border border-green-700">
              <h4 className="font-semibold text-green-300 mb-2">Why Area Charts for Volume Analysis?</h4>
              <p className="text-sm text-gray-300">
                Area charts emphasize the magnitude of change and are perfect for showing volume data. 
                The filled area helps visualize the "weight" of trading activity and cumulative effects.
              </p>
            </div>
            <ResponsiveContainer width="100%" height={400}>
              <AreaChart data={volumeData}>
                <defs>
                  <linearGradient id="volumeGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#3B82F6" stopOpacity={0.1}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="date" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }}
                  labelStyle={{ color: '#9CA3AF' }}
                />
                <Area 
                  type="monotone" 
                  dataKey="volume" 
                  stroke="#3B82F6" 
                  fillOpacity={1} 
                  fill="url(#volumeGradient)" 
                  strokeWidth={2}
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        );

      case 'candlestick':
        return (
          <div className="space-y-4">
            <div className="bg-purple-900/20 p-4 rounded-lg border border-purple-700">
              <h4 className="font-semibold text-purple-300 mb-2">Why Candlestick Charts for Trading?</h4>
              <p className="text-sm text-gray-300">
                Candlestick charts pack four data points (Open, High, Low, Close) into one visual element. 
                Essential for technical analysis, showing market sentiment and identifying reversal patterns.
              </p>
            </div>
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={candlestickData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis dataKey="date" stroke="#9CA3AF" />
                <YAxis stroke="#9CA3AF" />
                <Tooltip 
                  content={({ active, payload, label }) => {
                    if (active && payload && payload.length) {
                      const data = payload[0].payload;
                      const isGreen = data.close > data.open;
                      return (
                        <div className="bg-gray-900 p-3 rounded-lg border border-gray-700">
                          <p className="text-gray-300 mb-2">{label}</p>
                          <div className="space-y-1">
                            <p className="text-white">Open: ${data.open}</p>
                            <p className="text-white">High: ${data.high}</p>
                            <p className="text-white">Low: ${data.low}</p>
                            <p className={`font-semibold ${isGreen ? 'text-green-400' : 'text-red-400'}`}>
                              Close: ${data.close}
                            </p>
                          </div>
                        </div>
                      );
                    }
                    return null;
                  }}
                />
                <Bar dataKey="high" fill="transparent" />
                {candlestickData.map((entry, index) => {
                  const isGreen = entry.close > entry.open;
                  const bodyHeight = Math.abs(entry.close - entry.open);
                  const bodyY = Math.max(entry.open, entry.close);
                  
                  return (
                    <g key={index}>
                      {/* Wick lines */}
                      <line
                        x1={50 + index * 100}
                        y1={400 - (entry.high - 160) * 2}
                        x2={50 + index * 100}
                        y2={400 - (entry.low - 160) * 2}
                        stroke={isGreen ? '#10B981' : '#EF4444'}
                        strokeWidth={1}
                      />
                      {/* Body rectangle */}
                      <rect
                        x={35 + index * 100}
                        y={400 - (bodyY - 160) * 2}
                        width={30}
                        height={bodyHeight * 2}
                        fill={isGreen ? '#10B981' : '#EF4444'}
                        fillOpacity={0.8}
                      />
                    </g>
                  );
                })}
              </BarChart>
            </ResponsiveContainer>
          </div>
        );

      case 'bar':
        return (
          <div className="space-y-4">
            <div className="bg-yellow-900/20 p-4 rounded-lg border border-yellow-700">
              <h4 className="font-semibold text-yellow-300 mb-2">Why Bar Charts for Performance Comparison?</h4>
              <p className="text-sm text-gray-300">
                Bar charts excel at comparing discrete categories. Perfect for showing stock performance rankings, 
                making it easy to identify top and bottom performers at a glance.
              </p>
            </div>
            <ResponsiveContainer width="100%" height={400}>
              <BarChart data={performanceData} layout="horizontal">
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis type="number" stroke="#9CA3AF" />
                <YAxis dataKey="stock" type="category" stroke="#9CA3AF" />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }}
                  labelStyle={{ color: '#9CA3AF' }}
                  formatter={(value) => [`${value}%`, 'Performance']}
                />
                <Bar dataKey="performance" fill="#3B82F6" radius={[0, 4, 4, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        );

      case 'pie':
        return (
          <div className="space-y-4">
            <div className="bg-indigo-900/20 p-4 rounded-lg border border-indigo-700">
              <h4 className="font-semibold text-indigo-300 mb-2">Why Pie Charts for Portfolio Allocation?</h4>
              <p className="text-sm text-gray-300">
                Pie charts effectively show parts of a whole. Ideal for displaying portfolio composition, 
                sector allocation, or market share distribution. Easy to see proportional relationships.
              </p>
            </div>
            <div className="flex justify-center">
              <ResponsiveContainer width="100%" height={400}>
                <PieChart>
                  <Pie
                    data={sectorData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(1)}%`}
                    outerRadius={120}
                    fill="#8884d8"
                    dataKey="value"
                    animationDuration={800}
                  >
                    {sectorData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }}
                    formatter={(value) => [`${value}%`, 'Allocation']}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        );

        case 'scatter':
        return (
          <div className="space-y-4">
            <div className="bg-red-900/20 p-4 rounded-lg border border-red-700">
              <h4 className="font-semibold text-red-300 mb-2">Why Scatter Plots for Correlation Analysis?</h4>
              <p className="text-sm text-gray-300">
                Scatter plots reveal relationships between two variables. Perfect for analyzing correlations 
                between stocks, risk vs return analysis, or identifying outliers in the data.
              </p>
            </div>
            <ResponsiveContainer width="100%" height={400}>
              <ScatterChart data={correlationData}>
                <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                <XAxis 
                  type="number" 
                  dataKey="stock1" 
                  name="AAPL Price" 
                  stroke="#9CA3AF"
                  domain={['dataMin', 'dataMax']}
                />
                <YAxis 
                  type="number" 
                  dataKey="stock2" 
                  name="GOOGL Price" 
                  stroke="#9CA3AF"
                  domain={['dataMin', 'dataMax']}
                />
                <Tooltip 
                  cursor={{ strokeDasharray: '3 3' }}
                  contentStyle={{ backgroundColor: '#1F2937', border: '1px solid #374151' }}
                  formatter={(value, name) => [value, name === 'stock1' ? 'AAPL' : 'GOOGL']}
                />
                <Scatter dataKey="stock2" fill="#3B82F6" />
              </ScatterChart>
            </ResponsiveContainer>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-purple-900 text-white p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
            Chart Type Selection for Stock Market Analysis
          </h1>
          <p className="text-gray-300">Learn when and why to use different visualization types for financial insights</p>
        </div>

        {/* Chart Type Selector */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-8">
          {chartTypes.map((chart) => (
            <button
              key={chart.id}
              onClick={() => setActiveChart(chart.id)}
              className={`p-6 rounded-xl border-2 transition-all duration-200 text-left ${
                activeChart === chart.id
                  ? 'border-blue-500 bg-blue-900/30 shadow-lg shadow-blue-500/20'
                  : 'border-gray-700 bg-gray-800/30 hover:border-gray-600 hover:bg-gray-800/50'
              }`}
            >
              <div className="flex items-center space-x-3 mb-3">
                <div className={`p-2 rounded-lg ${
                  activeChart === chart.id ? 'bg-blue-500' : 'bg-gray-700'
                }`}>
                  {chart.icon}
                </div>
                <h3 className="font-semibold text-lg">{chart.name}</h3>
              </div>
              <p className="text-sm text-gray-400 mb-2">{chart.purpose}</p>
              <div className="text-xs">
                <p className="text-blue-300 mb-1"><strong>Best for:</strong> {chart.bestFor}</p>
                <p className="text-green-300"><strong>Insights:</strong> {chart.insights}</p>
              </div>
            </button>
          ))}
        </div>

        {/* Chart Display */}
        <div className="bg-gray-800/20 backdrop-blur-sm rounded-xl p-6 border border-gray-700">
          <div className="flex items-center space-x-3 mb-6">
            <div className="p-2 bg-blue-500 rounded-lg">
              {chartTypes.find(c => c.id === activeChart)?.icon}
            </div>
            <h2 className="text-2xl font-bold">
              {chartTypes.find(c => c.id === activeChart)?.name} Example
            </h2>
          </div>
          
          {renderChart()}
        </div>

        {/* Summary Guide */}
        <div className="mt-8 bg-gradient-to-r from-blue-900/20 to-purple-900/20 rounded-xl p-6 border border-blue-700/50">
          <h3 className="text-xl font-bold mb-4 text-center">Quick Selection Guide</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="font-semibold text-blue-300 mb-2">Time-Based Analysis:</h4>
              <ul className="space-y-1 text-sm text-gray-300">
                <li>• <strong>Line Charts:</strong> Price trends, comparative performance</li>
                <li>• <strong>Area Charts:</strong> Volume trends, cumulative returns</li>
                <li>• <strong>Candlesticks:</strong> Detailed price action, trading patterns</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-green-300 mb-2">Categorical Analysis:</h4>
              <ul className="space-y-1 text-sm text-gray-300">
                <li>• <strong>Bar Charts:</strong> Performance rankings, comparisons</li>
                <li>• <strong>Pie Charts:</strong> Portfolio allocation, market share</li>
                <li>• <strong>Scatter Plots:</strong> Correlations, risk-return analysis</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChartSelectionGuide;