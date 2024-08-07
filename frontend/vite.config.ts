import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  esbuild: {
    loader: 'js', // Use jsx loader for .js files
    include: /src\/.*\.js$/, // Apply only to .js files in the src directory
  },
});
