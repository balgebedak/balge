'use client'

import { useState } from 'react'

export default function Home() {
  const [prompt, setPrompt] = useState('')
  const [mainContent, setMainContent] = useState('')
  const [loading, setLoading] = useState(false)

  const handleGenerate = async () => {
    if (!prompt.trim()) return
    setLoading(true)

    try {
      const formData = new FormData()
      formData.append('prompt', prompt)

      const res = await fetch('http://127.0.0.1:8000/generate', {
        method: 'POST',
        body: formData,
      })

      const data = await res.json()

      const id = data.output_path.split('/').pop()
      const fileRes = await fetch(`http://127.0.0.1:8000/view/${id}`)
      const fileText = await fileRes.text()

      setMainContent(fileText)
    } catch (err) {
      console.error('Failed to generate project:', err)
      setMainContent('❌ Failed to fetch project')
    } finally {
      setLoading(false)
    }
  }

  return (
    <main className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">🧠 Balge App Generator</h1>

      <div className="flex gap-2">
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe your app (e.g., 'Make a calculator in Python')"
          className="p-2 border rounded w-full"
        />
        <button
          onClick={handleGenerate}
          className="bg-blue-600 text-white px-4 py-2 rounded"
          disabled={loading}
        >
          {loading ? 'Generating...' : 'Generate'}
        </button>
      </div>

      {mainContent && (
        <pre className="p-4 bg-black text-green-200 border rounded text-sm whitespace-pre-wrap">
          {mainContent}
        </pre>
      )}
    </main>
  )
}
