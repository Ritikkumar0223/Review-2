import React, { useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area, BarChart, Bar, PieChart, Pie, Cell } from 'recharts';
import { Eye, EyeOff, Palette, Zap, CheckCircle, XCircle, Lightbulb } from 'lucide-react';

const AestheticsGuide = () => {
  const [comparisonView, setComparisonView] = useState('poor');
  const [activeSection, setActiveSection] = useState('color');

  // Sample data
  const stockData = [
    { date: '2024-01', AAPL: 175.25, GOOGL: 142.56, TSLA: 248.42, volume: 48.3 },
    { date: '2024-02', AAPL: 181.86, GOOGL: 139.91, TSLA: 201.29, volume: 52.1 },
    { date: '2024-03', AAPL: 169.12, GOOGL: 141.75, TSLA: 175.79, volume: 58.7 },
    { date: '2024-04', AAPL: 185.43, GOOGL: 155.89, TSLA: 194.77, volume: 51.2 },
    { date: '2024-05', AAPL: 189.47, GOOGL: 138.21, TSLA: 234.86, volume: 54.2 }
  ];

  const sectorData = [
    { name: 'Technology', value: 28.5 },
    { name: 'Healthcare', value: 13.2 },
    { name: 'Financial', value: 11.8 },
    { name: 'Consumer', value: 10.9 },
    { name: 'Energy', value: 8.4 },
    { name: 'Others', value: 27.2 }
  ];

  // Poor vs Good color schemes
  const poorColors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff'];
  const goodColors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4'];

  const sections = [
    {
      id: 'color',
      title: 'Color Theory & Accessibility',
      icon: <Palette className="w-5 h-5" />,
      description: 'Strategic use of color for clarity and accessibility'
    },
    {
      id: 'typography',
      title: 'Typography & Labeling',
      icon: <Eye className="w-5 h-5" />,
      description: 'Clear, readable text and meaningful labels'
    },
    {
      id: 'layout',
      title: 'Layout & Spacing',
      icon: <Zap className="w-5 h-5" />,
      description: 'Organized visual hierarchy and breathing room'
    },
    {
      id: 'interactions',
      title: 'Interactive Elements',
      icon: <CheckCircle className="w-5 h-5" />,
      description: 'Intuitive user interactions and feedback'
    }
  ];

  const renderPoorExample = () => (
    <div className="bg-white p-4 rounded-lg border-2 border-red-400">
      <h3 className="text-xl font-bold text-black mb-2">STOCK PRICES!!!</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={stockData}>
          <XAxis dataKey="date" />
          <YAxis />
          <Line type="monotone" dataKey="AAPL" stroke="#ff0000" strokeWidth={1} />
          <Line type="monotone" dataKey="GOOGL" stroke="#00ff00" strokeWidth={1} />
          <Line type="monotone" dataKey="TSLA" stroke="#0000ff" strokeWidth={1} />
        </LineChart>
      </ResponsiveContainer>
      <div className="mt-2 text-xs text-red-600">
        <p>❌ Harsh, clashing colors</p>
        <p>❌ No grid or context</p>
        <p>❌ Poor typography</p>
        <p>❌ No tooltips or legend</p>
      </div>
    </div>
  );

  const renderGoodExample = () => (
    <div className="bg-gradient-to-br from-gray-50 to-blue-50 p-6 rounded-xl border border-gray-200 shadow-lg">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-2xl font-bold text-gray-800">Stock Price Trends</h3>
        <div className="text-sm text-gray-600">Last 5 months</div>
      </div>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={stockData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
          <XAxis 
            dataKey="date" 
            stroke="#6B7280"
            fontSize={12}
            tickFormatter={(value) => value.replace('2024-', '')}
          />
          <YAxis 
            stroke="#6B7280"
            fontSize={12}
            tickFormatter={(value) => `$${value}`}
          />
          <Tooltip 
            contentStyle={{ 
              backgroundColor: 'rgba(255, 255, 255, 0.95)', 
              border: '1px solid #E5E7EB',
              borderRadius: '8px',
              boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
            }}
            formatter={(value, name) => [`$${value}`, name]}
            labelFormatter={(label) => `Month: ${label}`}
          />
          <Legend 
            wrapperStyle={{ paddingTop: '20px' }}
            iconType="line"
          />
          <Line 
            type="monotone" 
            dataKey="AAPL" 
            stroke="#3B82F6" 
            strokeWidth={3}
            dot={{ r: 4, fill: '#3B82F6' }}
            activeDot={{ r: 6, stroke: '#3B82F6', strokeWidth: 2, fill: '#fff' }}
          />
          <Line 
            type="monotone" 
            dataKey="GOOGL" 
            stroke="#10B981" 
            strokeWidth={3}
            dot={{ r: 4, fill: '#10B981' }}
            activeDot={{ r: 6, stroke: '#10B981', strokeWidth: 2, fill: '#fff' }}
          />
          <Line 
            type="monotone" 
            dataKey="TSLA" 
            stroke="#F59E0B" 
            strokeWidth={3}
            dot={{ r: 4, fill: '#F59E0B' }}
            activeDot={{ r: 6, stroke: '#F59E0B', strokeWidth: 2, fill: '#fff' }}
          />
        </LineChart>
      </ResponsiveContainer>
      <div className="mt-4 text-sm text-green-600 space-y-1">
        <p>✅ Harmonious color palette</p>
        <p>✅ Clear grid and formatting</p>
        <p>✅ Professional typography</p>
        <p>✅ Interactive tooltips</p>
      </div>
    </div>
  );

  const renderColorSection = () => (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-red-50 p-6 rounded-xl border border-red-200">
          <h4 className="font-bold text-red-800 mb-3 flex items-center">
            <XCircle className="w-5 h-5 mr-2" />
            Poor Color Choices
          </h4>
          <div className="space-y-3">
            <div className="flex space-x-2">
              {poorColors.map((color, index) => (
                <div 
                  key={index}
                  className="w-8 h-8 rounded border"
                  style={{ backgroundColor: color }}
                />
              ))}
            </div>
            <ul className="text-sm text-red-700 space-y-1">
              <li>• Harsh, saturated colors</li>
              <li>• Poor contrast ratios</li>
              <li>• Clashing combinations</li>
              <li>• Not colorblind friendly</li>
            </ul>
          </div>
        </div>

        <div className="bg-green-50 p-6 rounded-xl border border-green-200">
          <h4 className="font-bold text-green-800 mb-3 flex items-center">
            <CheckCircle className="w-5 h-5 mr-2" />
            Good Color Choices
          </h4>
          <div className="space-y-3">
            <div className="flex space-x-2">
              {goodColors.map((color, index) => (
                <div 
                  key={index}
                  className="w-8 h-8 rounded border"
                  style={{ backgroundColor: color }}
                />
              ))}
            </div>
            <ul className="text-sm text-green-700 space-y-1">
              <li>• Balanced saturation</li>
              <li>• Accessible contrast</li>
              <li>• Harmonious palette</li>
              <li>• Colorblind accessible</li>
            </ul>
          </div>
        </div>
      </div>

      <div className="bg-blue-50 p-6 rounded-xl border border-blue-200">
        <h4 className="font-bold text-blue-800 mb-3 flex items-center">
          <Lightbulb className="w-5 h-5 mr-2" />
          Color Best Practices for Finance
        </h4>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm text-blue-700">
          <div>
            <p className="font-semibold mb-2">Semantic Colors:</p>
            <ul className="space-y-1">
              <li>• Green: Positive returns, gains</li>
              <li>• Red: Negative returns, losses</li>
              <li>• Blue: Neutral, primary data</li>
              <li>• Orange: Warnings, volatility</li>
            </ul>
          </div>
          <div>
            <p className="font-semibold mb-2">Accessibility:</p>
            <ul className="space-y-1">
              <li>• Minimum 4.5:1 contrast ratio</li>
              <li>• Use patterns with color</li>
              <li>• Test with colorblind simulators</li>
              <li>• Provide alternative indicators</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );

  const renderTypographySection = () => (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-gray-100 p-6 rounded-xl">
          <h4 className="font-bold text-gray-800 mb-4">Poor Typography Example</h4>
          <div className="space-y-3">
            <h5 className="text-xs text-gray-600">stock chart</h5>
            <div className="text-lg font-bold text-black">AAPL: $189.47</div>
            <div className="text-xs text-gray-500">change: +2.34 (+1.25%)</div>
            <div className="text-xs text-gray-400">volume: 54.2M market cap: 2.94T</div>
          </div>
          <div className="mt-4 text-xs text-red-600">
            <p>❌ Inconsistent sizing</p>
            <p>❌ Poor hierarchy</p>
            <p>❌ Hard to scan</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-xl border border-gray-200 shadow-sm">
          <h4 className="font-bold text-gray-800 mb-4">Good Typography Example</h4>
          <div className="space-y-3">
            <h5 className="text-sm font-medium text-gray-600 uppercase tracking-wide">Apple Inc.</h5>
            <div className="flex items-baseline space-x-2">
              <span className="text-3xl font-bold text-gray-900">$189.47</span>
              <span className="text-lg text-green-600 font-semibold">+2.34 (+1.25%)</span>
            </div>
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span className="text-gray-500">Volume</span>
                <span className="ml-2 font-medium">54.2M</span>
              </div>
              <div>
                <span className="text-gray-500">Market Cap</span>
                <span className="ml-2 font-medium">$2.94T</span>
              </div>
            </div>
          </div>
          <div className="mt-4 text-xs text-green-600">
            <p>✅ Clear hierarchy</p>
            <p>✅ Consistent spacing</p>
            <p>✅ Easy to scan</p>
          </div>
        </div>
      </div>

      <div className="bg-purple-50 p-6 rounded-xl border border-purple-200">
        <h4 className="font-bold text-purple-800 mb-3">Typography Guidelines</h4>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-purple-700">
          <div>
            <p className="font-semibold mb-2">Hierarchy:</p>
            <ul className="space-y-1">
              <li>• Primary: 24-32px</li>
              <li>• Secondary: 18-24px</li>
              <li>• Body: 14-16px</li>
              <li>• Captions: 12-14px</li>
            </ul>
          </div>
          <div>
            <p className="font-semibold mb-2">Spacing:</p>
            <ul className="space-y-1">
              <li>• Consistent line height</li>
              <li>• Adequate margins</li>
              <li>• Logical grouping</li>
              <li>• White space usage</li>
            </ul>
          </div>
          <div>
            <p className="font-semibold mb-2">Readability:</p>
            <ul className="space-y-1">
              <li>• Sans-serif for screens</li>
              <li>• 45-75 characters per line</li>
              <li>• High contrast text</li>
              <li>• Avoid all caps</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );

  const renderLayoutSection = () => (
    <div className="space-y-6">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-gray-200 p-2 rounded-lg">
          <h4 className="font-bold text-gray-800 mb-2 text-center">Cluttered Layout</h4>
          <div className="bg-white p-2 rounded" style={{ fontSize: '10px' }}>
            <div className="flex justify-between items-center mb-1">
              <span>AAPL</span><span>$189.47</span><span>+2.34</span>
            </div>
            <ResponsiveContainer width="100%" height={120}>
              <LineChart data={stockData.slice(0, 3)}>
                <Line dataKey="AAPL" stroke="#3B82F6" strokeWidth={1} />
              </LineChart>
            </ResponsiveContainer>
            <div className="flex text-xs">
              <span>Vol:54.2M</span><span>Cap:2.94T</span><span>PE:28.4</span>
            </div>
          </div>
          <div className="mt-2 text-xs text-red-600">
            <p>❌ Cramped spacing</p>
            <p>❌ No visual hierarchy</p>
            <p>❌ Information overload</p>
          </div>
        </div>

        <div className="bg-gradient-to-br from-blue-50 to-indigo-50 p-6 rounded-xl border border-blue-200">
          <div className="flex justify-between items-center mb-6">
            <div>
              <h4 className="text-xl font-bold text-gray-800">Apple Inc.</h4>
              <p className="text-sm text-gray-600">NASDAQ: AAPL</p>
            </div>
            <div className="text-right">
              <div className="text-2xl font-bold text-gray-900">$189.47</div>
              <div className="text-sm text-green-600 font-medium">+2.34 (+1.25%)</div>
            </div>
          </div>
          
          <ResponsiveContainer width="100%" height={120}>
            <LineChart data={stockData.slice(0, 3)}>
              <Line 
                dataKey="AAPL" 
                stroke="#3B82F6" 
                strokeWidth={2}
                dot={false}
              />
            </LineChart>
          </ResponsiveContainer>
          
          <div className="grid grid-cols-3 gap-4 mt-6 text-sm">
            <div className="text-center">
              <div className="text-gray-500">Volume</div>
              <div className="font-semibold">54.2M</div>
            </div>
            <div className="text-center">
              <div className="text-gray-500">Market Cap</div>
              <div className="font-semibold">$2.94T</div>
            </div>
            <div className="text-center">
              <div className="text-gray-500">P/E Ratio</div>
              <div className="font-semibold">28.4</div>
            </div>
          </div>
          
          <div className="mt-4 text-xs text-green-600">
            <p>✅ Generous spacing</p>
            <p>✅ Clear sections</p>
            <p>✅ Logical flow</p>
          </div>
        </div>
      </div>

      <div className="bg-indigo-50 p-6 rounded-xl border border-indigo-200">
        <h4 className="font-bold text-indigo-800 mb-3">Layout Principles</h4>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h5 className="font-semibold text-indigo-700 mb-2">Visual Hierarchy</h5>
            <ul className="text-sm text-indigo-600 space-y-1">
              <li>• Most important info first</li>
              <li>• Size indicates importance</li>
              <li>• Group related elements</li>
              <li>• Use consistent alignment</li>
            </ul>
          </div>
          <div>
            <h5 className="font-semibold text-indigo-700 mb-2">White Space</h5>
            <ul className="text-sm text-indigo-600 space-y-1">
              <li>• Improves readability</li>
              <li>• Creates focus areas</li>
              <li>• Reduces cognitive load</li>
              <li>• Appears more professional</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );

  const renderInteractionsSection = () => (
    <div className="space-y-6">
      <div className="bg-gray-50 p-6 rounded-xl">
        <h4 className="font-bold text-gray-800 mb-4">Interactive Best Practices</h4>
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart data={stockData}>
            <defs>
              <linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3B82F6" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#3B82F6" stopOpacity={0.1}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />
            <XAxis 
              dataKey="date" 
              stroke="#6B7280"
              fontSize={12}
            />
            <YAxis 
              stroke="#6B7280"
              fontSize={12}
            />
            <Tooltip 
              contentStyle={{ 
                backgroundColor: 'rgba(255, 255, 255, 0.95)', 
                border: '1px solid #E5E7EB',
                borderRadius: '12px',
                boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1)',
                padding: '12px'
              }}
              formatter={(value, name) => [
                `$${value.toFixed(2)}`, 
                name === 'AAPL' ? 'Apple Inc.' : name
              ]}
              labelFormatter={(label) => `Period: ${label}`}
              cursor={{ fill: 'rgba(59, 130, 246, 0.1)' }}
            />
            <Area 
              type="monotone" 
              dataKey="AAPL" 
              stroke="#3B82F6" 
              fill="url(#colorGradient)"
              strokeWidth={3}
              dot={{ r: 4, fill: '#3B82F6', strokeWidth: 2, stroke: '#fff' }}
              activeDot={{ 
                r: 8, 
                fill: '#3B82F6', 
                stroke: '#fff', 
                strokeWidth: 3,
                filter: 'drop-shadow(0 4px 6px rgba(0, 0, 0, 0.1))'
              }}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-green-50 p-6 rounded-xl border border-green-200">
          <h5 className="font-bold text-green-800 mb-3">Tooltip Design</h5>
          <div className="space-y-2 text-sm text-green-700">
            <p>✅ Contextual information</p>
            <p>✅ Readable formatting</p>
            <p>✅ Subtle animations</p>
            <p>✅ Non-intrusive styling</p>
          </div>
        </div>

        <div className="bg-blue-50 p-6 rounded-xl border border-blue-200">
          <h5 className="font-bold text-blue-800 mb-3">Hover Effects</h5>
          <div className="space-y-2 text-sm text-blue-700">
            <p>✅ Visual feedback</p>
            <p>✅ Highlight active elements</p>
            <p>✅ Smooth transitions</p>
            <p>✅ Cursor indicators</p>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-blue-50 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-2 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
            Aesthetics & Clarity in Financial Visualizations
          </h1>
          <p className="text-gray-600 text-lg">Master the art of creating clear, beautiful, and accessible data visualizations</p>
        </div>

        {/* Before/After Comparison */}
        <div className="mb-8">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-2xl font-bold text-gray-800">Before vs After Comparison</h2>
            <div className="flex bg-gray-200 rounded-lg p-1">
              <button
                onClick={() => setComparisonView('poor')}
                className={`px-4 py-2 rounded-md transition-all ${
                  comparisonView === 'poor' 
                    ? 'bg-red-500 text-white shadow-md' 
                    : 'text-gray-600 hover:bg-gray-300'
                }`}
              >
                Poor Design
              </button>
              <button
                onClick={() => setComparisonView('good')}
                className={`px-4 py-2 rounded-md transition-all ${
                  comparisonView === 'good' 
                    ? 'bg-green-500 text-white shadow-md' 
                    : 'text-gray-600 hover:bg-gray-300'
                }`}
              >
                Good Design
              </button>
            </div>
          </div>
          
          <div className="mb-6">
            {comparisonView === 'poor' ? renderPoorExample() : renderGoodExample()}
          </div>
        </div>

        {/* Section Navigation */}
        <div className="mb-8">
          <div className="flex flex-wrap gap-2">
            {sections.map((section) => (
              <button
                key={section.id}
                onClick={() => setActiveSection(section.id)}
                className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
                  activeSection === section.id
                    ? 'bg-blue-500 text-white shadow-md'
                    : 'bg-white text-gray-600 hover:bg-gray-100 border border-gray-200'
                }`}
              >
                {section.icon}
                <span className="font-medium">{section.title}</span>
              </button>
            ))}
          </div>
        </div>

        {/* Section Content */}
        <div className="mb-8">
          <div className="mb-4">
            <h2 className="text-2xl font-bold text-gray-800">
              {sections.find(s => s.id === activeSection)?.title}
            </h2>
            <p className="text-gray-600">
              {sections.find(s => s.id === activeSection)?.description}
            </p>
          </div>
          
          {activeSection === 'color' && renderColorSection()}
          {activeSection === 'typography' && renderTypographySection()}
          {activeSection === 'layout' && renderLayoutSection()}
          {activeSection === 'interactions' && renderInteractionsSection()}
        </div>

        {/* Summary Guidelines */}
        <div className="bg-white p-8 rounded-xl shadow-lg border border-gray-200">
          <h3 className="text-2xl font-bold text-gray-800 mb-6 text-center">
            Essential Aesthetic Principles for Financial Data
          </h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-3">
                <Palette className="w-8 h-8 text-blue-600" />
              </div>
              <h4 className="font-bold text-gray-800 mb-2">Color Harmony</h4>
              <p className="text-sm text-gray-600">Use consistent, accessible color schemes that convey meaning</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-3">
                <Eye className="w-8 h-8 text-green-600" />
              </div>
              <h4 className="font-bold text-gray-800 mb-2">Clear Typography</h4>
              <p className="text-sm text-gray-600">Establish hierarchy with consistent, readable fonts</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-3">
                <Zap className="w-8 h-8 text-purple-600" />
              </div>
              <h4 className="font-bold text-gray-800 mb-2">Smart Layout</h4>
              <p className="text-sm text-gray-600">Organize information with proper spacing and alignment</p>
            </div>
            
            <div className="text-center">
              <div className="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-3">
                <CheckCircle className="w-8 h-8 text-orange-600" />
              </div>
              <h4 className="font-bold text-gray-800 mb-2">User Experience</h4>
              <p className="text-sm text-gray-600">Provide intuitive interactions and helpful feedback</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AestheticsGuide;