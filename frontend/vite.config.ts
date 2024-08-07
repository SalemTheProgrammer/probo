import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import { config } from 'dotenv';

// Load environment variables from .env file
config();

export default defineConfig({
  plugins: [react()],
  define: {
    'process.env': process.env,
  },
  esbuild: {
    loader: 'js', // Use jsx loader for .js files
    include: /src\/.*\.js$/, // Apply only to .js files in the src directory
  },
});
